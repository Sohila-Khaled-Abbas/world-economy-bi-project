"""
Unit tests for data_ingestion.py
--------------------------------
Validates:
- World Bank loader combines multiple sheets
- HDI loader reads CSV correctly
- Merge step joins correctly on 'Country Code'
"""

import pandas as pd
import pytest
from pathlib import Path

# Import the functions from your ingestion script
import sys
sys.path.append("src")
from data_ingestion import load_world_bank_data, load_hdi_data, merge_datasets


@pytest.fixture
def mock_world_bank_excel(tmp_path):
    """Creates a mock Excel file with two sheets for testing."""
    file = tmp_path / "WorldBank.xlsx"
    sheet1 = pd.DataFrame({"Country Code": ["AAA", "BBB"], "GDP": [100, 200]})
    sheet2 = pd.DataFrame({"Country Code": ["CCC", "DDD"], "GDP": [300, 400]})
    with pd.ExcelWriter(file) as writer:
        sheet1.to_excel(writer, sheet_name="Sheet1", index=False)
        sheet2.to_excel(writer, sheet_name="Sheet2", index=False)
    return file


@pytest.fixture
def mock_hdi_csv(tmp_path):
    """Creates a mock HDI CSV file for testing."""
    file = tmp_path / "HDI.csv"
    df = pd.DataFrame({"Country Code": ["AAA", "CCC"], "HDI": [0.8, 0.9]})
    df.to_csv(file, index=False)
    return file


def test_load_world_bank_data(mock_world_bank_excel):
    df = load_world_bank_data(mock_world_bank_excel)
    assert isinstance(df, pd.DataFrame)
    assert "source_sheet" in df.columns
    assert df.shape[0] == 4  # two sheets x two rows each


def test_load_hdi_data(mock_hdi_csv):
    df = load_hdi_data(mock_hdi_csv)
    assert isinstance(df, pd.DataFrame)
    assert "HDI" in df.columns
    assert df.shape[0] == 2


def test_merge_datasets(mock_world_bank_excel, mock_hdi_csv):
    wb_df = load_world_bank_data(mock_world_bank_excel)
    hdi_df = load_hdi_data(mock_hdi_csv)
    merged = merge_datasets(wb_df, hdi_df)

    assert isinstance(merged, pd.DataFrame)
    assert "HDI" in merged.columns
    # Check merge: AAA and CCC should have HDI, BBB and DDD should be NaN
    hdi_values = merged.set_index("Country Code")["HDI"].to_dict()
    assert hdi_values["AAA"] == 0.8
    assert pd.isna(hdi_values["BBB"])
    assert hdi_values["CCC"] == 0.9
    assert pd.isna(hdi_values["DDD"])

from pandera.errors import SchemaError

def test_schema_validation_fails_on_bad_data(tmp_path):
    bad_df = pd.DataFrame({"Country Code": ["AAA"], "GDP": ["NotANumber"]})
    with pytest.raises(SchemaError):
        from data_ingestion import WorldBankSchema
        WorldBankSchema.validate(bad_df)
