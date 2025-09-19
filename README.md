# 🌍 Global Economy Analysis (World Bank + HDI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project%20Status-Active-success)
![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)
![Live Preview](https://img.shields.io/badge/▶%20Live%20Preview-Click%20to%20View-green?style=for-the-badge)](images/dashboard_preview.gif)


A **data-driven one-page report** on the state of the global economy using World Bank and UN HDI datasets.  
This project covers the full **ETL pipeline**, schema validation, profiling, and insight generation — preparing data for **Power BI dashboarding**.

---

## 🚀 What’s included

```markdown
| Folder/File                                        | Description                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------- |
| `src/data_ingestion.py`                            | Python ETL (Extract + Merge + Save) with schema validation                        |
| `tests/test_data_ingestion.py`                     | Automated unit tests (pytest) for ingestion & merge                               |
| `notebooks/01_data_profiling_and_validation.ipynb` | Post-ingestion QA & profiling notebook (schema validation + missing data heatmap) |
| `data/processed_data.csv`                          | Cleaned dataset produced by ETL notebook                                          |
| `reports/BUILD_PBIX.md`                            | Step-by-step guide + DAX code for Power BI                                        |
| `powerbi/GlobalEconomy.pbix`                       | Final dashboard (binary file)                                                     |
| `reports/images/`                                  | Profiling visualizations & histograms                                             |
| `images/`                                          | Dashboard preview & pipeline diagram                                              |
| `requirements.txt`                                 | Reproducible Python environment                                                   |
```

---

## 📂 Dataset Description

```markdown
| Dataset                     | Source               | Records | Fields | Format |
| --------------------------- | -------------------- | ------- | ------ | ------ |
| **World Bank Indicators**   | World Bank Open Data | 12,657  | 58     | Excel  |
| **Human Development Index** | United Nations       | ~200    | 2      | CSV    |
```

Key fields used:  
`GDP (USD)`, `GDP per capita (USD)`, `Year`, `Country Code`, `Region`, `Life Expectancy`, `Power Consumption`, `HDI`.

---

## 🔧 Project Pipeline

![Project Pipleine.png](/images/Project%20Pipeline.png)

1. **Extract** → Load multi-sheet Excel + HDI CSV (`src/data_ingestion.py`)
2. **Validate** → Schema check with [Pandera](https://pandera.readthedocs.io)
3. **Transform** → Filter 2014, calculate population, join HDI
4. **Profile** → EDA notebook (skimpy + missing data heatmap)
5. **Load** → Save data`/processed_data.csv`
6. **Visualize** → Build Power BI report using [BUILD_PBIX.md](/reports/BUILD_PBIX.md)
7. **Insights** → Export dashboard screenshots + correlation summary

---

## ⚙️ Setup & Installation

1. Clone the repo and install dependencies:

```bash
git clone https://github.com/Sohila-Khaled-Abbas/global-economy-analysis.git
cd global-economy-analysis

# Install dependencies
pip install -r requirements.txt
```

2. Run ETL:

```bash
python src/data_ingestion.py
```

3. Run tests:

```bash
pytest -v
```

4. Run profiling notebook:

```bash
jupyter notebook 
notebooks/data_profiling_and_validation.ipynb
```

---

## 🛠 Building the Power BI Dashboard

Follow [BUILD_PBIX.md](/reports/BUILD_PBIX.md) for **click-by-click** **instructions** & paste-ready DAX.

- Standardize column names in Power Query
- Create measures: `TotalGDP`, `TotalPopulationM`, `Avg_HDI`, `Corr_GDPpc_HDI_2014`
- Build visuals: Stacked area GDP & population, Bubble chart (Life vs GDPpc), HDI bar chart, Power vs GDP scatter
- Add bookmarks for storytelling & tooltip pages for country drill-through

---

## 📊 Key Insights (2014)

```markdown
| Metric                              | Insight                                   |
| ----------------------------------- | ----------------------------------------- |
| Correlation (GDP per Capita vs HDI) | **0.85** (Strong positive correlation)    |
| Population Distribution             | Asia & Africa account for most population |
| HDI Ranking                         | Europe highest, Africa lowest             |
```

### Sample histograms

![GDP_(USD)_hist](/reports/images/GDP_(USD)_hist.png)
![GDP_per_capita_hist](/reports/images/GDP_per_capita_(USD)_hist.png)
![HDI_hist](/reports/images/HDI_hist.png)
![Population_(M)_hist](/reports/images/Population_(M)_hist.png)

---

## 📷 Preview

See more charts in `reports/images/`.

---

## 🧪 Testing & QA

 **Unit tests** in `tests/test_data_ingestion.py` check:
- Excel sheet combination
- CSV load
- Left-join correctness on Country Code

**Schema validation** ensures key columns exist (Country Code, GDP, GDP per Capita)

**Profiling notebook** generates:

- Summary stats
- Missing value heatmap
- Key distribution histograms


---

## 🧭 Roadmap

- Automate ETL with Prefect/Airflow + GitHub Actions
- Publish interactive Power BI report (Power BI Service)
- Add more indicators (education, inequality, emissions)
- Deploy to GitHub Pages with interactive profiling report

---

## 📜 License

This project is licensed under the [MIT License](/LICENSE) — feel free to use and adapt it.

---

## 👩‍💻 Author

**Sohila Khaled Galal Abbas**
*Data Analyst & Power BI Developer*
🔗 [LinkedIn](www.linkedin.com/in/sohilakabbas) • [GitHub](https://github.com/Sohila-Khaled-Abbas)
