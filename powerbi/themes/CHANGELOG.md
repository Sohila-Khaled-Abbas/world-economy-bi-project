# 📝 Theme Changelog – Global Economy Dashboard

This file tracks changes made to the Power BI theme (`global_economy.json`).  
Follow [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`) when updating.

---

## [1.0.0] – 2025-09-17
### Added
- Initial release of `global_economy.json`
- Included:
  - **Color palette:** 7 region-specific, color-blind safe colors
  - **Typography:** Defined text classes for titles, headers, and labels
  - **Visual defaults:** Minimal borders, subtle gridlines, consistent padding

---

## [1.1.0] – YYYY-MM-DD
### Changed
- 🎨 Updated color for Sub-Saharan Africa to improve contrast on dark backgrounds  
- 🔤 Increased font size for card labels from `16` → `18`  

---

## [1.1.1] – YYYY-MM-DD
### Fixed
- 🐛 Corrected table header background to meet WCAG contrast compliance  
- 🐛 Fixed alignment of category axis labels on stacked area charts  

---

## [2.0.0] – YYYY-MM-DD
### Breaking Changes
- 🔄 Switched from default Segoe UI to custom corporate font  
- 🧹 Major redesign of layout defaults: removed gridlines from all visuals except line/area charts  

---

## 🧑‍💻 How to Update
1. Open `global_economy.json`  
2. Make necessary edits (e.g., colors, font sizes)  
3. Bump version number:
   - MAJOR → If you completely change the visual identity (breaking change)
   - MINOR → If you add new features (new visuals, colors, styles)
   - PATCH → If you fix a small issue or tweak a setting
4. Document changes under the new version heading in this file  

---

## 📌 Maintenance Tips
- Always test theme changes on all visuals before releasing.
- If used across multiple PBIX projects, commit theme updates to each repo to avoid version drift.
- Keep this changelog in sync with Git commits (e.g., reference commit SHA if using GitHub).

---

> 💡 **Pro Tip:** Add a tag to your Git repo (`git tag v1.0.0`) whenever you release a new theme version — this helps you roll back quickly if a theme change breaks a report layout.
