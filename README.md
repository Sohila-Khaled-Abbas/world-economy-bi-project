# 🌍 Global Economy Insights (BI + Python Project)

![Dashboard Preview](images/dashboard_preview.png)

## 📌 Project Overview

This project analyzes global economic development data from the **World Bank** and **United Nations Human Development Index (HDI)**.  
It demonstrates a full **Business Intelligence workflow**:

- Data cleaning & profiling (Python)
- Data transformation (Power Query)
- Interactive dashboard development (Power BI)

---

## 🗂 Project Structure

| Folder | Contents |
|-------|-----------|
| **data/** | Raw and processed data files |
| **notebooks/** | Python Jupyter notebook for data cleaning & profiling |
| **reports/** | HTML profiling report + PDF export of dashboard |
| **powerbi/** | Power BI file (`.pbix`) |
| **images/** | Dashboard screenshots for README and documentation |

---

## 🚀 Workflow

1. **Data Preparation (Python):**
   - Import World Bank and HDI data
   - Calculate `Population (M)` using GDP & GDP per Capita
   - Merge with HDI data on `Country Code`
   - Generate automated profiling report with `ydata-profiling`

2. **Data Transformation (Power BI):**
   - Create `gdp_pivot`, `pop_pivot`, `wb_hdi_by_region` tables
   - Perform data type checks and relationship setup in Power BI model

3. **Visualization (Power BI):**
   - Stacked area charts for GDP & Population
   - Bubble chart (Life Expectancy vs GDP per Capita vs Population)
   - Bar chart (Average HDI by Region)
   - Scatterplot (Power Consumption vs GDP per Capita, colored by HDI)

4. **Reporting:**
   - One-page Power BI dashboard with title and narrative context
   - Key takeaway: **GDP per Capita and HDI correlation = 0.85 (2014)**

---

## 📊 Key Insights

- **East Asia & Pacific** led global GDP growth in 2014.
- **Sub-Saharan Africa** had the highest population growth.
- Strong positive correlation (**0.85**) between GDP per Capita and HDI.

---

## 🛠 Tech Stack

- **Python** (`pandas`, `ydata-profiling`)
- **Power BI** (Data modeling, DAX, visuals)
- **Excel + CSV** (Data source)

---

## 📷 Dashboard Preview

![Key Insights](images/key_insights.png)

---

## 📥 Installation

Clone this repo and install Python dependencies:

```bash
git clone https://github.com/<your-username>/world-economy-bi-project.git
cd world-economy-bi-project
pip install -r requirements.txt
```

---

## 📌 Requirements

```nginx
pandas
ydata-profiling
openpyxl
```

---

## 📢 Contributing

Pull requests and suggestions are welcome!
Feel free to open issues for improvements or add new visuals/metrics.

---

## 👩‍💻 Author

Sohila Khaled Galal Abbas
Data Analyst | Power BI Developer | Python Enthusiast
[LinkedIn](www.linkedin.com/in/sohilakabbas)