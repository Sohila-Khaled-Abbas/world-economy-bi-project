---
name: "🚀 Release Checklist"
about: "Use this template to prepare a new release of the Power BI dashboard and theme."
title: "Release vX.X.X"
labels: ["release", "QA", "PowerBI"]
assignees: []
---

# 🚀 Release Checklist – Global Economy Dashboard

## 🗓 Release Info
- **Version:** `vX.X.X`
- **Release Date:** `YYYY-MM-DD`
- **Author:** @yourusername

---

## ✅ Pre-Release QA

- [ ] **Data Refresh:** Run `notebooks/global_economy_etl.ipynb` and confirm `processed_data.csv` is up-to-date
- [ ] **Column Schema:** Ensure column names and types match Power Query expectations
- [ ] **DAX Measures:** Validate calculations (Total GDP, Population, HDI, Correlation)
- [ ] **Visual Consistency:**
  - [ ] Region colors match theme
  - [ ] Slicers and filters work
  - [ ] Tooltips display correct info
  - [ ] Drillthrough pages function as expected
- [ ] **Accessibility:** Check font sizes, color contrast, and keyboard navigation
- [ ] **Performance:** Verify PBIX file size and page load times are acceptable
- [ ] **Theme Version:** Ensure `global_economy.json` version number is correct

---

## 📝 Changelog Updates

- [ ] Update `themes/CHANGELOG.md` with new version and changes
- [ ] Commit changes with semantic commit message (`chore(release): vX.X.X`)

---

## 📦 Build & Tag

- [ ] Save final PBIX to `powerbi/global_economy_dashboard.pbix`
- [ ] Export latest dashboard preview image to `images/dashboard_collage.png`
- [ ] Tag release in Git:  
```bash
git add .
git commit -m "chore(release): vX.X.X"
git tag vX.X.X
git push origin main --tags
```

---

## 📤 GitHub Release

- [ ] Draft a new release on GitHub
- [ ] Attach .pbix, preview image, and changelog notes
- [ ] Publish release

---

## 🧪 Post-Release Validation

- [ ] Open release .pbix on a clean machine to ensure no broken visuals
- [ ] Verify interactive slicers/bookmarks work as expected
- [ ] Share dashboard link (if published to Power BI Service)

---

> 🧠 **Pro Tip**: Use GitHub Actions or a manual CI step to automatically validate file size and schema before pushing a release.