# 🧪 Power BI Theme QA Checklist
**Theme:** `global_economy.json`  
**Version:** (update with current version)  

Use this checklist before merging theme changes into `main` or tagging a new release.  
This ensures that **colors, fonts, gridlines, and layout consistency** are preserved across visuals.

---

## 🎨 Color Verification

- [ ] **Region Colors**: Confirm that all region-based visuals use the same color mapping:  
  | Region                     | Expected Color |
  | -------------------------- | -------------- |
  | Europe & Central Asia      | `#1f77b4`      |
  | East Asia & Pacific        | `#ff7f0e`      |
  | Sub-Saharan Africa         | `#2ca02c`      |
  | Latin America & Caribbean  | `#d62728`      |
  | Middle East & North Africa | `#9467bd`      |
  | North America              | `#8c564b`      |
  | South Asia                 | `#e377c2`      |

- [ ] **KPI Status Colors:** Good = green, Bad = red, Neutral = gray.

---

## 🖋️ Typography Verification

- [ ] **Titles:** Segoe UI Semibold, 13pt, black  
- [ ] **Legends:** Segoe UI, 10pt, black  
- [ ] **Axis Labels:** Segoe UI, 10pt, dark gray  
- [ ] **Cards:** Values bold, at least 20pt; Category labels smaller (11pt)  
- [ ] **Table Headers:** Segoe UI Semibold, 11pt, gray background  
- [ ] **Table Values:** Segoe UI, 10pt, dark text

---

## 📊 Visual Layout Consistency

- [ ] **Stacked Area Charts:** Gridlines visible but subtle (`#e0e0e0` dotted)  
- [ ] **Tables:** Row padding = 4px, alternating row colors clear  
- [ ] **Legends:** Positioned at TopCenter or Right consistently  
- [ ] **Scatter/Bubble Charts:** Font size of axes & legend matches area charts  
- [ ] **No Unexpected Borders/Drop Shadows:** Confirm all visuals have clean edges

---

## ⚙️ Functional Checks

- [ ] Import theme successfully without errors in Power BI  
- [ ] Check that slicers inherit font style & color correctly  
- [ ] Confirm tooltips are legible on light background  
- [ ] Verify that bookmarks maintain theme styling after switching pages

---

## 🧑‍💻 Developer Notes

- [ ] Increment version number in `themes/CHANGELOG.md`  
- [ ] Commit theme change with semantic message:  
  ```bash
  git commit -m "style(theme): update font sizes and gridline color (v1.0.X)"
  ```
- [ ] If major redesign, tag release (e.g., v2.0.0) and update documentation

---

> 💡 **Pro Tip**: Keep a small "theme test" PBIX with all major visual types (cards, tables, bar, area, scatter) to quickly verify changes in one place before rolling out to production dashboards.


