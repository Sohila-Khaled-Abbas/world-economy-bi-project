# 🌍 Global Economy Analysis (World Bank + HDI)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project%20Status-Active-success)
![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)
![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange)

A **data-driven one-page report** on the state of the global economy using World Bank and UN HDI datasets.  
This project covers the full **ETL pipeline**, exploratory data analysis, and insight generation — preparing data for **Power BI dashboarding**.

---

## 📑 Table of Contents

- [🌍 Global Economy Analysis (World Bank + HDI)](#-global-economy-analysis-world-bank--hdi)
  - [📑 Table of Contents](#-table-of-contents)
  - [📖 About the Project](#-about-the-project)
  - [📂 Dataset Description](#-dataset-description)
  - [🔧 Project Pipeline](#-project-pipeline)
  - [📁 Folder Structure](#-folder-structure)
  - [⚙️ Setup \& Installation](#️-setup--installation)
  - [📊 Results \& Insights](#-results--insights)
    - [Sample histograms](#sample-histograms)
  - [Future Improvements](#future-improvements)
  - [📜 License](#-license)
  - [👩‍💻 Author](#-author)

---

## 📖 About the Project

This project demonstrates **Business Intelligence Project Management best practices**:

- 🔄 **ETL (Extract, Transform, Load)** pipeline using Python  
- 📊 **Data Profiling** with `skimpy`  
- 📈 **One-page Power BI report** summarizing economic insights  
- 💡 **Actionable metrics**: GDP, GDP per Capita, Population, HDI, Life Expectancy  

The notebook is **fully reproducible** — it auto-installs dependencies and saves processed outputs for easy visualization in Power BI or any BI tool.

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

## 📁 Folder Structure

```wasm
📦 global-economy-analysis
├── data
│   ├── WorldBank.xlsx
│   ├── HDI.csv
│   └── processed_data.csv
├── notebooks
│   └── global_economy_etl.ipynb
├── reports
│   └── images/
│       ├── GDP_hist.png
│       ├── GDP_per_Capita_hist.png
│       ├── Population_(M)_hist.png
│       └── HDI_hist.png
├── README.md
└── LICENSE
```

---

## ⚙️ Setup & Installation

Clone the repo and run the notebook:

```bash
Copy code
git clone https://github.com/Sohila-Khaled-Abbas/global-economy-analysis.git
cd global-economy-analysis

# Launch Jupyter
jupyter notebook notebooks/global_economy_etl.ipynb

# Install dependencies
pip install -r requirements.txt

```
Dependencies are installed automatically by the notebook (`pandas`, `matplotlib`, `skimpy`).


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

## Future Improvements

- Add Power BI .pbix dashboard to the repo
- Automate ETL pipeline with Airflow or Prefect
- Add more indicators (education, inequality, emissions)
- Deploy interactive dashboard via GitHub Pages or Streamlit

---

## 📜 License

This project is licensed under the [MIT License](/LICENSE) — feel free to use and adapt it.

---

## 👩‍💻 Author

**Sohila Khaled Galal Abbas**
*Data Analyst & Power BI Developer*
🔗 [LinkedIn](www.linkedin.com/in/sohilakabbas) • [GitHub](https://github.com/Sohila-Khaled-Abbas)