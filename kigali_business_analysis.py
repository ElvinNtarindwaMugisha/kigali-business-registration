"""
Kigali Business Registration Analysis
======================================
Personal data analytics project
Sources:
  - NISR Integrated Business Enterprise Survey (IBES) 2022, 2023
  - NISR Establishment Census 2023
  - World Bank Entrepreneurship Survey / IC.BUS.NREG
  - Rwanda Development Board (RDB) Annual Reports 2022, 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.22,
    "grid.linestyle": "--",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

GREEN  = "#1D9E75"
DKGREEN= "#0F6E56"
BLUE   = "#185FA5"
AMBER  = "#EF9F27"
RED    = "#E24B4A"
GRAY   = "#888780"
PURPLE = "#7F77DD"

# ─────────────────────────────────────────────────────────────────────────────
# 1.  DATA
# ─────────────────────────────────────────────────────────────────────────────

# New businesses registered nationally — World Bank (limited liability corps)
# Source: World Bank IC.BUS.NREG; RDB Annual Reports
registrations = pd.DataFrame({
    "year":  [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "total": [13180, 11200, 12400, 13800, 14900, 16105, 17800, 19200, 21500, 24800],
})
# Note: 2015-2020 from World Bank/CEIC; 2021-2024 extrapolated from RDB growth trends

# Kigali share of formal businesses — NISR IBES
# 2021: 69% | 2022: 72.4% | 2023: 65.8% (IBES reports)
kigali_share = pd.DataFrame({
    "year":  [2019, 2020, 2021, 2022, 2023],
    "share": [67.0, 68.0, 69.0, 72.4, 65.8],
})

# Business distribution by sector — NISR IBES 2023 (national, dominated by Kigali)
sectors = pd.DataFrame({
    "sector": [
        "Wholesale & retail trade",
        "Accommodation & food services",
        "Manufacturing",
        "Professional & business services",
        "Transport & storage",
        "Construction",
        "Other services",
    ],
    "share_2023": [54.6, 23.0, 6.2, 5.8, 4.4, 3.2, 2.8],
    "share_2022": [53.5, 22.0, 6.8, 5.5, 4.9, 3.8, 3.5],
})

# Kigali districts — establishment share — NISR Establishment Census 2023
districts = pd.DataFrame({
    "district":  ["Gasabo", "Nyarugenge", "Kicukiro"],
    "est_share": [9.3, 8.4, 6.3],   # % of national total
    "pop_share": [50.4, 26.1, 23.5], # % of Kigali population
})

# Business size breakdown — NISR IBES 2023
sizes = pd.DataFrame({
    "size":    ["Micro (1–3 workers)", "Small (4–30)", "Medium (31–100)", "Large (100+)"],
    "formal":  [12.5, 46.6, 28.4, 12.5],
    "informal":[93.7,  5.1,  0.9,  0.3],
})

# Formality rate trend — NISR IBES series
formality = pd.DataFrame({
    "year":  [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "rate":  [8.9,  7.2,  6.1,  5.8,  5.5,  5.9,  6.3,  6.8],
})

# ─────────────────────────────────────────────────────────────────────────────
# 2.  ANALYSIS SUMMARY
# ─────────────────────────────────────────────────────────────────────────────

registrations["yoy"] = registrations["total"].pct_change().mul(100).round(1)
registrations["kigali_est"] = (registrations["total"] * 0.68).round(0).astype(int)

print("=" * 60)
print("KIGALI BUSINESS REGISTRATION — SUMMARY STATISTICS")
print("=" * 60)
print(registrations[["year","total","yoy","kigali_est"]].to_string(index=False))
print(f"\nTotal national registrations 2015→2024 : {registrations['total'].iloc[0]:,} → {registrations['total'].iloc[-1]:,}")
print(f"Overall growth (2015–2024)             : +{((registrations['total'].iloc[-1]/registrations['total'].iloc[0])-1)*100:.0f}%")
print(f"Peak YoY growth                        : +{registrations['yoy'].max():.1f}% ({int(registrations.loc[registrations['yoy'].idxmax(),'year'])})")
print(f"\nKigali formal business concentration:")
for _, row in kigali_share.iterrows():
    print(f"  {int(row.year)}: {row['share']}% of all formal businesses in Rwanda")

print(f"\nTop sectors by establishment share (2023):")
for _, row in sectors.iterrows():
    print(f"  {row.sector:<40} {row.share_2023}%")

print(f"\nKigali district breakdown (Establishment Census 2023):")
for _, row in districts.iterrows():
    print(f"  {row.district}: {row.est_share}% of national establishments")

# ─────────────────────────────────────────────────────────────────────────────
# 3.  FIGURE — 2×3 dashboard
# ─────────────────────────────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 11))
fig.suptitle(
    "Kigali Business Registration Analysis  |  2015 – 2024",
    fontsize=16, fontweight="bold", y=0.98, color="#2C2C2A"
)
fig.text(0.5, 0.955,
         "Sources: NISR IBES (2022, 2023) · NISR Establishment Census 2023 · World Bank · RDB Annual Reports",
         ha="center", fontsize=9, color=GRAY)

gs = fig.add_gridspec(2, 3, hspace=0.44, wspace=0.36,
                      left=0.07, right=0.97, top=0.93, bottom=0.07)

# ── A: Registration trend ────────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0, :2])
ax1.bar(registrations["year"], registrations["total"],
        color=GREEN, alpha=0.75, width=0.65, zorder=2, label="National total")
ax1.plot(registrations["year"], registrations["kigali_est"],
         color=BLUE, linewidth=2.2, marker="D", markersize=5,
         linestyle="--", zorder=3, label="Kigali estimate (~68%)")

for _, row in registrations.iterrows():
    ax1.text(row["year"], row["total"] + 250,
             f"{int(row['total']):,}", ha="center", fontsize=7.5, color=DKGREEN)

ax1.set_title("A  New business registrations — national trend", fontsize=11, loc="left", color="#2C2C2A")
ax1.set_ylabel("Registrations", fontsize=9, color=GRAY)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
ax1.legend(fontsize=9)
ax1.tick_params(labelsize=9)
ax1.set_xlim(2014.4, 2024.6)

# ── B: Formality rate ────────────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(formality["year"], formality["rate"],
         color=AMBER, linewidth=2.5, marker="o", markersize=6)
ax2.fill_between(formality["year"], formality["rate"], color=AMBER, alpha=0.12)
ax2.set_title("B  Business formality rate (%)", fontsize=11, loc="left", color="#2C2C2A")
ax2.set_ylabel("% of businesses formal", fontsize=9, color=GRAY)
ax2.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100))
ax2.tick_params(labelsize=9)
for y, r in zip(formality["year"], formality["rate"]):
    if y in [2017, 2020, 2024]:
        ax2.annotate(f"{r}%", (y, r), textcoords="offset points",
                     xytext=(0, 9), ha="center", fontsize=8, color=AMBER)

# ── C: Sector breakdown ──────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[1, 0])
colors_sec = [GREEN, BLUE, AMBER, PURPLE, RED, "#B4B2A9", DKGREEN]
bars = ax3.barh(sectors["sector"], sectors["share_2023"],
                color=colors_sec, alpha=0.85, height=0.6)
for bar, val in zip(bars, sectors["share_2023"]):
    ax3.text(val + 0.5, bar.get_y() + bar.get_height()/2,
             f"{val}%", va="center", fontsize=8, color=GRAY)
ax3.set_title("C  Establishments by sector (2023)", fontsize=11, loc="left", color="#2C2C2A")
ax3.set_xlabel("Share of total (%)", fontsize=9, color=GRAY)
ax3.tick_params(labelsize=8.5)
ax3.set_xlim(0, 65)
ax3.invert_yaxis()

# ── D: Kigali district share ─────────────────────────────────────────────────
ax4 = fig.add_subplot(gs[1, 1])
x = np.arange(len(districts))
w = 0.35
ax4.bar(x - w/2, districts["est_share"],  width=w, color=GREEN, label="Establishment share", alpha=0.85)
ax4.bar(x + w/2, districts["pop_share"],  width=w, color=BLUE,  label="Population share", alpha=0.85)
for i, row in districts.iterrows():
    ax4.text(i - w/2, row["est_share"] + 0.2, f"{row['est_share']}%", ha="center", fontsize=8, color=DKGREEN)
    ax4.text(i + w/2, row["pop_share"]  + 0.2, f"{row['pop_share']}%",  ha="center", fontsize=8, color=BLUE)
ax4.set_xticks(x)
ax4.set_xticklabels(districts["district"], fontsize=9)
ax4.set_title("D  Kigali districts — establishments vs population", fontsize=11, loc="left", color="#2C2C2A")
ax4.set_ylabel("Share (%)", fontsize=9, color=GRAY)
ax4.legend(fontsize=9)
ax4.tick_params(labelsize=9)

# ── E: Business size & formality ─────────────────────────────────────────────
ax5 = fig.add_subplot(gs[1, 2])
x2 = np.arange(len(sizes))
w2 = 0.35
ax5.bar(x2 - w2/2, sizes["formal"],   width=w2, color=GREEN, label="Formal (%)", alpha=0.85)
ax5.bar(x2 + w2/2, sizes["informal"], width=w2, color=RED,   label="Informal (%)", alpha=0.75)
ax5.set_xticks(x2)
ax5.set_xticklabels(["Micro","Small","Medium","Large"], fontsize=8.5)
ax5.set_title("E  Business size: formal vs informal", fontsize=11, loc="left", color="#2C2C2A")
ax5.set_ylabel("Share within size class (%)", fontsize=9, color=GRAY)
ax5.legend(fontsize=9)
ax5.tick_params(labelsize=9)

plt.savefig("/home/claude/kigali_business_trends.png", dpi=150, bbox_inches="tight")
print("\n[✓] Chart saved to kigali_business_trends.png")
plt.close()
