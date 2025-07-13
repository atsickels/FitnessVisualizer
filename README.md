**Project Name:** Fitness Progress Visualizer

**Overview:**
A Python-based data visualization project that starts as a script and can evolve into a Flask web app. It processes exported fitness data (primarily from Hevy in CSV format) and compares it to average benchmarks from public datasets. The main focus is on learning Python syntax with a long-term goal of expanding into full-stack development with Flask.

---

**Core Goals:**
- Practice and learn Python syntax in a practical, real-world setting
- Visualize fitness progress through graphs and reports
- Compare personal progress to public/average data
- Build a project with a clear upgrade path to a web app (Flask)

---

**Project Scope (Phase 1 – Python Script):**
- Load and parse exported CSV workout logs from Hevy
- Visualize personal fitness data:
  - Line graphs of weight lifted over time for key exercises
  - Bar charts or tables showing weekly volume
  - PR progression for selected exercises
- Begin building comparison capability using aggregate fitness data (see "Data Sources" below)

**Stretch Features:**
- Summary report of recent PRs, best weeks, etc.
- Ability to generate charts/images to be saved locally
- Weekly/monthly muscle group focus charts
- Modular code ready for Flask integration

---

**Project Scope (Phase 2 – Flask Web App):**
- Create a Flask app with basic HTML templates
- Allow users to upload CSVs
- Render visualizations in-browser
- API endpoints for future integration or data serving

---

**Visualization Preferences:**
- Line charts (e.g., PR progression, volume over time)
- Ranking-style charts or tables
- Timeline-style insights and summaries

---

**Data Sources:**
1. **User Data:** CSV exports from Hevy (manually uploaded or read from local directory)
2. **External/Aggregate Data:**
   - Goal: Compare user's progress against average lifters or benchmarks based on height, weight, and gender
   - Priority for research and implementation

---

**Libraries/Tools:**
- `pandas` (data manipulation)
- `matplotlib` or `plotly` (data visualization)
- `csv` (file parsing)
- `Flask` (Phase 2)

---

**Next Steps:**
1. Research public datasets or APIs that include fitness benchmarks by gender, height, weight, or age
2. Build Python CSV importer and sample data visualizer for personal data
3. Design modular architecture for easy migration to Flask

