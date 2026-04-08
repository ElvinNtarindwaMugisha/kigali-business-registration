# Kigali Business Registration Analysis (2015–2024)

A data analytics project examining business registration trends, sectoral composition, formality rates, and district-level concentration across Kigali — Rwanda's economic capital. Kigali consistently accounts for over 65% of all formal business activity in Rwanda, making it the primary lens through which to understand Rwanda's private sector growth.

---

## Live Dashboard

Open `Kigali_Business_Dashboard.html` in any browser to explore the interactive charts, or view the PDF report for the full written analysis.

---

## Project Structure

```
kigali-business-registration/
│
├── Kigali_Business_Dashboard.html          # Interactive dashboard (open in browser)
├── Kigali_Business_Registration_Analysis.pdf  # Full written report with tables & charts
├── kigali_business_analysis.py             # Python analysis script
└── README.md
```

---

## Key Findings

- **65.8%** of all formal businesses in Rwanda are based in Kigali (NISR IBES 2023)
- New business registrations grew **+88%** nationally between 2015 and 2024 (13,180 → 24,800)
- **Wholesale & retail trade** dominates at 54.6% of all establishments; **accommodation & food services** at 23% reflects Kigali's growing MICE and tourism economy
- **87% of businesses are informal** — meaning official registration data captures only a fraction of actual business activity; micro enterprises (83.9% of all businesses) operate 93.7% informally
- **Nyarugenge** is Kigali's most commercially dense district (density index 0.32), anchored by the central business district
- **Gasabo** leads in raw establishment count (9.3% of national total) while **Kicukiro** is the fastest-growing industrial zone
- The only registration dip was **2016 (−15%)**; every other year showed growth, with 2024 posting the strongest year at **+15.3%**

---

## Tools & Skills Demonstrated

| Area | Tools / Methods |
|---|---|
| Data wrangling | Python, pandas |
| Visualisation | matplotlib (5-panel figure), Chart.js (HTML dashboard) |
| Statistical analysis | YoY % change, concentration ratios, density index |
| Reporting | ReportLab (PDF generation) |
| Dashboard | HTML, CSS, JavaScript |

---

## Data Sources

All data is from official, publicly available sources:

- **NISR** — Integrated Business Enterprise Survey (IBES) 2022, December 2023
- **NISR** — Integrated Business Enterprise Survey (IBES) 2023, March 2025
- **NISR** — Establishment Census 2023 (statistics.gov.rw)
- **NISR / World Bank** — Rwanda IBES 2019–2021 Report, March 2023
- **World Bank** — New Businesses Registered indicator (IC.BUS.NREG), Rwanda 2006–2020
- **Rwanda Development Board (RDB)** — Annual Reports 2022 and 2024 (rdb.rw)

---

## How to Run the Python Script

Make sure you have Python 3 installed, then:

```bash
pip install pandas matplotlib numpy
python kigali_business_analysis.py
```

This will print a full summary table to the terminal and save a 5-panel chart image (`kigali_business_trends.png`) to your working directory.

---

## About

This project pulled business registration data from the NISR Integrated Business Enterprise Survey (IBES 2022 and 2023), the NISR Establishment Census 2023, the World Bank entrepreneurship indicator (IC.BUS.NREG), and RDB Annual Reports. The data was cleaned and structured in pandas, with year-on-year growth rates, Kigali concentration estimates, and a district-level density index (establishment share ÷ population share) computed from scratch. A 5-panel matplotlib figure was generated covering the registration trend, sector breakdown, formality rate, formal vs informal by business size, and district comparisons. Findings were compiled into a structured PDF report using ReportLab, and an interactive HTML dashboard was built with Chart.js featuring four live charts, a district deep-dive section, and a full data table — all grounded in real official Rwandan statistics.
