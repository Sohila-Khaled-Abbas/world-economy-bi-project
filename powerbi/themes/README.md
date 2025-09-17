# 🎨 Power BI Theme – Global Economy Dashboard

This folder contains the **Power BI theme file** used in the Global Economy Dashboard:  

- **File:** `global_economy.json`
- **Purpose:** Define consistent colors, fonts, and layout defaults for all visuals in the report.

---

## 📥 How to Apply This Theme

1. Open your `.pbix` file in Power BI Desktop.
2. Go to **View → Themes → Browse for themes**.
3. Select `global_economy.json`.
4. Click **Open** — the theme will apply instantly to all visuals.

---

## 🎯 Why This Theme Matters

✅ **Consistent Color Palette:**  
Regions are color-coded with a color-blind safe palette:
| Region                     | Hex Color |
| -------------------------- | --------- |
| Europe & Central Asia      | `#1f77b4` |
| East Asia & Pacific        | `#ff7f0e` |
| Sub-Saharan Africa         | `#2ca02c` |
| Latin America & Caribbean  | `#d62728` |
| Middle East & North Africa | `#9467bd` |
| North America              | `#8c564b` |
| South Asia                 | `#e377c2` |

✅ **Clean Layout Defaults:**  
Minimal borders, subtle gridlines, and consistent font sizes reduce visual noise.

✅ **Accessibility:**  
Colors meet WCAG contrast guidelines, and visual hierarchies are preserved for better readability.

---

## 🛠 Customizing for Future Projects

- **Colors:** Edit `dataColors` array in the JSON file to match your brand or region scheme.
- **Typography:** Modify `textClasses` to change font face/size across all visuals.
- **Visual Defaults:** Add or remove sections under `visualStyles` to enforce chart-specific formatting (e.g., card labels, table outlines).

---

## 🧠 Developer Tips

- **Version Control:**  
  - Use semantic versioning in the JSON (`"version": "1.0.0"`).
  - Bump version number when making changes for easier tracking.

- **Theme Consistency:**  
  - Apply the same theme to drillthrough pages, tooltip pages, and bookmarks to avoid jarring visual changes.

- **Testing:**  
  - After applying the theme, review all visuals:
    - Check if region colors are correctly mapped.
    - Verify that font sizes are readable in all visual types (especially bar charts & tooltips).

- **Reuse Across Projects:**  
  - Copy this theme into `/themes/` folder of future Power BI projects for a consistent design system.
  - Keep a `themes/CHANGELOG.md` to track modifications across projects.

---

## 📚 Resources

- [Microsoft Theme JSON Schema](https://learn.microsoft.com/power-bi/create-reports/desktop-report-themes#theme-json-schema)
- [Accessible Color Palettes](https://colorbrewer2.org/)
- [Power BI Theme Samples](https://github.com/microsoft/powerbi-desktop-samples)

---

> 💡 **Pro Tip:** When sharing your `.pbix` on GitHub, include both the PBIX and theme file — this lets others reproduce the exact look and feel of your dashboard without manual formatting.
