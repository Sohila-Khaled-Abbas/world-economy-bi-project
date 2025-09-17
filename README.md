# 🌍 Global Economy Analysis (World Bank + HDI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project%20Status-Active-success)
![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)
[![PBIX QA Workflow](https://github.com/Sohila-Khaled-Abbas/world-economy-bi-project/.github/workflows/pbix-qa.yml/badge.svg)](https://github.com/Sohila-Khaled-Abbas/world-economy-bi-project/.github/workflows/pbix-qa.yml)
> **Status:** This badge shows whether the latest commit on `main` passed all quality checks (data validation, theme check, PBIX size check).

A **data-driven one-page report** on the state of the global economy using World Bank and UN HDI datasets.  
This project covers the full **ETL pipeline**, exploratory data analysis, and insight generation — preparing data for **Power BI dashboarding**.

---

## 🚀 What’s included

- `data/processed_data.csv` — cleaned dataset produced by ETL notebook.
- `notebooks/global_economy_etl.ipynb` — ETL and profiling steps (skimpy).
- `powerbi/GlobalEconomy.pbix` — Power BI dashboard (final deliverable).
- `reports/` — generated profiling HTML & images.
- `images/` — dashboard previews & story graphics.
- `README.md`, `LICENSE`, `.gitignore`, `requirements.txt`.

---

## 📂 Dataset Description

| Dataset                     | Source               | Records | Fields | Format |
| --------------------------- | -------------------- | ------- | ------ | ------ |
| **World Bank Indicators**   | World Bank Open Data | 12,657  | 58     | Excel  |
| **Human Development Index** | United Nations       | ~200    | 2      | CSV    |

Key fields used:  
`GDP (USD)`, `GDP per capita (USD)`, `Year`, `Country Code`, `Region`, `Life Expectancy`, `Power Consumption`, `HDI`.

---

## 🔧 Project Pipeline

```mermaid
flowchart LR
    A[Extract Data] --> B[Transform & Clean]
    B --> C[Profile Data]
    C --> D[Load Processed Dataset]
    D --> E[Visualize in Power BI]
```

1. **Extract** – Import Excel + CSV data
2. **Transform** – Filter 2014, calculate population, join HDI
3. **Profile** – Summary statistics + histograms
4. **Load** – Save processed CSV
5. **Insights** – Correlation analysis + recommendations


---

## ⚙️ Setup & Installation

1. Clone the repo and run the notebook:

```bash
Copy code
git clone https://github.com/Sohila-Khaled-Abbas/global-economy-analysis.git
cd global-economy-analysis
```

2. Install Python deps and run notebook (optional):

```python
# Launch Jupyter
jupyter notebook notebooks/global_economy_etl.ipynb

# Install dependencies
pip install -r requirements.txt
# Run cells to regenerate data/processed_data.csv and reports/
```

*Dependencies are installed automatically by the notebook (`pandas`, `matplotlib`, `skimpy`).*

3. Open Power BI:

- File → Open → `powerbi/GlobalEconomy.pbix` **(or)** Home → Get Data → Text/CSV → select `data/processed_data.csv` then follow Build steps below.

---

## 🛠 How to rebuild the PBIX (exact steps)

*Follow the step-by-step instructions in [`BUILD_PBIX.md`](/reports/BUILD_PBIX.md) (or see the “Build the .pbix — step-by-step” section of this README).*

### Key points:

- Standardize column names in Power Query (Country, CountryCode, Region, Year, GDP_USD, GDP_per_Capita_USD, Population_M, HDI, Life_Expectancy, Power_kWh_per_capita).
- Create measures: `TotalGDP`, `TotalPopulationM`, `Avg_HDI`, `Corr_GDPpc_HDI_2014` (exact DAX included in BUILD_PBIX.md).
- Build visuals: stacked area GDP/pop, bubble chart, HDI by region, power vs GDP scatter.
- Add bookmarks for storytelling and a tooltip page for Country details.

---

## 📊 Results & Insights

```markdown
| Metric                              | Key Insight                                   |
| ----------------------------------- | --------------------------------------------- |
| Correlation (GDP per Capita vs HDI) | 0.82 (Strong positive)                        |
| Population Distribution             | Asia & Africa hold majority of population     |
| HDI Ranking                         | Europe has highest average HDI, Africa lowest |
```

### Sample histograms

![GDP_(USD)_hist](/reports/images/GDP_(USD)_hist.png)
![GDP_per_capita_hist](/reports/images/GDP_per_capita_(USD)_hist.png)
![HDI_hist](/reports/images/HDI_hist.png)
![Population_(M)_hist](/reports/images/Population_(M)_hist.png)

---

## 📷 Preview

See `images/dashboard.png` and `reports/images/` for profiling visuals.

---

## ⚙️ Reproducibility & Notes

- Use **Import** mode for best performance in Power BI.
- `powerbi/GlobalEconomy.pbix` is binary — large files may be better hosted as a release asset.
- Keep `data/` out of the repo if any dataset is sensitive (see `.gitignore`).

---

## 🧭 Next steps & improvements

- Automate ETL with Prefect/Airflow and CI.
- Add more indicators (education, inequality, emissions).
- Publish an interactive Power BI app and attach story slides.



---

## 📜 License

This project is licensed under the [MIT License](/LICENSE) — feel free to use and adapt it.

---

## 👩‍💻 Author

**Sohila Khaled Galal Abbas**
*Data Analyst & Power BI Developer*
🔗 [LinkedIn](www.linkedin.com/in/sohilakabbas) • [GitHub](https://github.com/Sohila-Khaled-Abbas)
