"""
Data Ingestion Script for Global Economy Project
------------------------------------------------
This script handles data ingestion (Extract step in ETL):
- Reads World Bank Excel file with multiple sheets
- Reads UN HDI CSV file
- Performs light schema normalization
- Outputs a single merged DataFrame ready for transformation

Author: Sohila Khaled Galal Abbas
Date: 2025-09-17
"""

import pandas as pd
import pandera as pa
from pathlib import Path

# Minimum schema expected by the World Bank GDP ingestion path.
# strict=False permits additional indicator columns from source workbooks.
WorldBankSchema = pa.DataFrameSchema(
    {
        "Country Code": pa.Column(str, nullable=False),
        "GDP": pa.Column(float, nullable=True),
    },
    strict=False,
)

# ---------- CONFIGURATION ----------
DATA_DIR = Path("D:\\courses\\Data Science\\Projects\\Python\\world-economy-bi-project\\data")
WORLD_BANK_FILE = DATA_DIR / "WorldBank.xlsx"
HDI_FILE = DATA_DIR / "HDI.csv"


def load_world_bank_data(filepath: Path) -> pd.DataFrame:
    """
    Loads multiple sheets from World Bank Excel file and combines them into a single DataFrame.

    Args:
        filepath (Path): Path to the Excel file

    Returns:
        pd.DataFrame: Combined DataFrame with all economic indicators
    """
    print(f"📥 Loading World Bank data from {filepath}...")
    xls = pd.ExcelFile(filepath)
    sheets = xls.sheet_names

    print(f"🔎 Found sheets: {sheets}")

    dfs = []
    for sheet in sheets:
        df_sheet = pd.read_excel(filepath, sheet_name=sheet)
        df_sheet["source_sheet"] = sheet  # track origin sheet
        dfs.append(df_sheet)

    df_combined = pd.concat(dfs, ignore_index=True)
    print(f"✅ Combined World Bank data shape: {df_combined.shape}")
    return df_combined


def load_hdi_data(filepath: Path) -> pd.DataFrame:
    """
    Loads HDI CSV data.

    Args:
        filepath (Path): Path to the CSV file

    Returns:
        pd.DataFrame: HDI data
    """
    print(f"📥 Loading HDI data from {filepath}...")
    df_hdi = pd.read_csv(filepath)
    print(f"✅ HDI data shape: {df_hdi.shape}")
    return df_hdi


def merge_datasets(world_bank_df: pd.DataFrame, hdi_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merges World Bank and HDI data on 'Country Code'.

    Args:
        world_bank_df (pd.DataFrame): World Bank data
        hdi_df (pd.DataFrame): HDI data

    Returns:
        pd.DataFrame: Merged dataset
    """
    if "Country Code" not in world_bank_df.columns or "Country Code" not in hdi_df.columns:
        raise KeyError("❌ 'Country Code' must exist in both datasets to perform merge.")

    print("🔗 Merging datasets on 'Country Code'...")
    df_merged = pd.merge(world_bank_df, hdi_df, on="Country Code", how="left")
    print(f"✅ Merged dataset shape: {df_merged.shape}")
    return df_merged


def main():
    """Runs the data ingestion pipeline."""
    world_bank_df = load_world_bank_data(WORLD_BANK_FILE)
    hdi_df = load_hdi_data(HDI_FILE)
    merged_df = merge_datasets(world_bank_df, hdi_df)

    # Save intermediate result for inspection
    output_file = DATA_DIR / "ingested_data.csv"
    merged_df.to_csv(output_file, index=False)
    print(f"💾 Saved ingested dataset to {output_file}")


if __name__ == "__main__":
    main()
