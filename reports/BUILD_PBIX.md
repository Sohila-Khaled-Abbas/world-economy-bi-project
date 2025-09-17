# 🏗️ Power BI Dashboard Build Guide  

**Project:** Global Economy Analysis  
**Author:** Sohila Khaled Galal Abbas  
**Deliverable:** `global_economy_dashboard.pbix`  

---

## 📂 Overview  

This document provides **exact, reproducible steps** to build the Power BI dashboard using the processed dataset (`data/processed_data.csv`).  
It follows the **ETL → Modeling → Visualization → Storytelling** flow, so anyone can clone this repo and rebuild the `.pbix` in minutes.

---

## 1️⃣ Extract & Load Data  

1. **Open Power BI Desktop**
2. Go to **Home → Get Data → Text/CSV**
3. Select `data/processed_data.csv`
4. Click **Load**

💡 *Tip:* Use a relative path if you keep the file inside this repo — this will make your PBIX portable.  

---

## 2️⃣ Transform Data (Power Query)  

1. Open **Transform Data** to launch Power Query  
2. Validate **data types**:  

| Column              | Type           |
| ------------------- | -------------- |
| `Year`              | Whole Number   |
| `GDP`               | Decimal Number |
| `GDP per Capita`    | Decimal Number |
| `Population (M)`    | Decimal Number |
| `Power Consumption` | Decimal Number |
| `HDI`               | Decimal Number |

3. **Remove nulls** for critical fields:  
   - `GDP`, `GDP per Capita`, `HDI`  
   *(Home → Remove Rows → Remove Blank Rows)*  

4. Close & Apply  

---

## 3️⃣ Create DAX Measures  

Go to **Modeling → New Measure** and create each of the following:  

```DAX
-- 💰 Total GDP
Total GDP = SUM('processed_data'[GDP])

-- 👥 Total Population
Total Population = SUM('processed_data'[Population (M)])

-- 📊 Average HDI
Average HDI = AVERAGE('processed_data'[HDI])

-- 🧮 GDP per Capita (Recalc)
GDP per Capita Calc = DIVIDE([Total GDP], [Total Population], 0)

-- 📈 GDP YoY Growth %
GDP YoY Growth % =
VAR CurrentYear = SELECTEDVALUE('processed_data'[Year])
VAR PrevYear = CurrentYear - 1
VAR GDPCurrent = CALCULATE([Total GDP], 'processed_data'[Year] = CurrentYear)
VAR GDPPrev = CALCULATE([Total GDP], 'processed_data'[Year] = PrevYear)
RETURN
DIVIDE(GDPCurrent - GDPPrev, GDPPrev, 0)
```

💡 *Tip:* Prefix measures with icons or tags (`💰`, `📊`) to make them easily identifiable in the Fields pane.

---

## 4️⃣ Build Visuals

### 📈 Stacked Area Chart – GDP Growth

- **Visual**: Stacked Area
- **Axis**: `Year`
- **Legend**: `Region`
- **Values**: `[Total GDP]`
- **Format**: Use consistent colors for `Region` (apply later to all visuals)

---

### 📈 Stacked Area Chart – Population Growth

- Duplicate previous visual
- Replace **Values** with `[Total Population]`

---

### 🔵 Bubble Chart – Life Expectancy vs GDP per Capita

```markdown
| Setting    | Value                             |
| ---------- | --------------------------------- |
| **Visual** | Scatter/Bubble                    |
| **X-Axis** | `Life Expectancy`                 |
| **Y-Axis** | `GDP per Capita` *(log scale ON)* |
| **Size**   | `Population (M)`                  |
| **Legend** | `Region`                          |
```

---

### 📊 Bar Chart – Average HDI by Region

- **Visual**: Clustered Bar
- **Axis**: Region
- **Values**: [Average HDI]
- **Sort**: Descending by [Average HDI]

---

### 🔍 Scatterplot – Power Consumption vs GDP per Capita

```markdown
| Setting    | Value                            |
| ---------- | -------------------------------- |
| **Visual** | Scatter                          |
| **X-Axis** | `Power Consumption`              |
| **Y-Axis** | `GDP per Capita`                 |
| **Color**  | `HDI` (Gradient Color Scale)     |
| **Filter** | Exclude outliers (e.g., Iceland) |
```

---

## 5️⃣ Assemble the Dashboard

### 1. Layout

#### Use a 3-row grid

- Row 1 → GDP + Population Area Charts
- Row 2 → Bubble Chart + HDI Bar Chart
- Row 3 → Power Consumption Scatter

### 2. Title & Context

Add a text box at the top:

```text
State of the Global Economy – 2014 Insights
```

And a subtitle:

```text
An interactive dashboard highlighting GDP, population growth, HDI distribution,
and economic development relationships across regions.
```

### 3. Theme

- Apply a custom JSON theme (optional, see `/powerbi/themes/global_economy.json`)
- Ensure region colors are consistent across visuals

---

## 6️⃣ Final Touches & Publishing

- Add Tooltips: show GDP per Capita, HDI, Population when hovering
- Adjust fonts and spacing for a clean, professional look
- Save as global_economy_dashboard.pbix
- (Optional) Publish to Power BI Service to share online

---

## ✅ Deliverable

By following this guide, you will produce:

- `global_economy_dashboard.pbix`
- A single-page, interactive report ready for presentation or GitHub showcase

📷 *See preview images in* [`/images/`](/images/)

---

> 💡 **Pro Tip**: Commit your PBIX + screenshots in `/images/` to GitHub so recruiters can preview your work without downloading the file.