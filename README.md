# Seasonal Agriculture Performance Analysis

## VOIS For Tech / AICTE Data Analytics Internship — Major Project

**Student Name:** Krishna Kumar  
**College Name:** Ambalika Institute of Management and Technology  
**AICTE STU ID:** STU6a252b77248381780820855  
**Course Certificate:** Data Visualization (ID: VFLMS26_163451)  
**GitHub Repository:** [https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis](https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis)

---

### Project Overview

This project analyzes **4,000 agricultural farm records** across three seasons (Kharif, Rabi, Zaid), eight crops, eight Indian states, and four irrigation methods. The analysis investigates seasonal differences in agricultural performance by identifying patterns, trends, relationships, and variations.

### Dataset

- **File:** `seasonal_agriculture_performance_dataset.csv`
- **Records:** 4,000 rows × 28 columns
- **Seasons:** Kharif (1,779), Rabi (1,627), Zaid (594)
- **Crops:** Chilli, Cotton, Groundnut, Maize, Pulses, Rice, Sugarcane, Wheat
- **States:** Andhra Pradesh, Gujarat, Karnataka, Madhya Pradesh, Maharashtra, Punjab, Tamil Nadu, Telangana

### Project Structure

```
VOIS/
├── seasonal_agriculture_performance_dataset.csv   # Original dataset (not modified)
├── Seasonal_Agriculture_Performance_Analysis.ipynb # Complete Jupyter Notebook
├── charts/                                        # All 12 analysis charts (PNG)
│   ├── 01_avg_yield_by_season.png
│   ├── 02_avg_profit_by_season.png
│   ├── 03_total_production_by_season.png
│   ├── 04_rainfall_vs_yield.png
│   ├── 05_temperature_vs_yield.png
│   ├── 06_water_usage_by_season.png
│   ├── 07_water_efficiency_by_season.png
│   ├── 08_disease_risk_by_season.png
│   ├── 09_crop_wise_avg_yield.png
│   ├── 10_irrigation_vs_yield.png
│   ├── 11_irrigation_vs_water_efficiency.png
│   └── 12_correlation_heatmap.png
├── VOIS_Project_PPT.pptx                          # Completed presentation (14 slides)
├── Certificate.pdf                                # Official course completion certificate
├── README.md                                      # This file
├── MANUAL_INSERTION_CHECKLIST.md                   # Items to fill manually
└── FINAL_VERIFICATION_REPORT.md                   # Verification results
```

### How to Run the Analysis

#### Prerequisites
```
pip install pandas numpy matplotlib seaborn jupyter
```

#### Running the Notebook
1. Open terminal in the project directory
2. Run: `jupyter notebook Seasonal_Agriculture_Performance_Analysis.ipynb`
3. Execute all cells (Kernel → Restart & Run All)
4. Charts are saved automatically to `charts/` directory

### Analysis Summary

The notebook covers:
1. **Data Understanding** — Dataset inspection, missing values, statistics
2. **Data Cleaning** — Median imputation for 120 missing values
3. **Season-wise Analysis** — Yield, production, profit by season
4. **Crop-wise Analysis** — Performance comparison across 8 crops
5. **Environmental Analysis** — Rainfall, temperature effects
6. **Irrigation Analysis** — Yield and water efficiency by method
7. **Economic Analysis** — Revenue, cost, profit patterns
8. **Correlation Analysis** — Relationships between key variables
9. **Key Findings** — 13 evidence-based findings
10. **Recommendations** — 5 practical recommendation areas

### Technologies Used

- **Python 3** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Jupyter Notebook** — Interactive development environment

### Key Findings

| Metric | Kharif | Rabi | Zaid |
|---|---|---|---|
| Avg Yield (t/ha) | 5.64 | 5.08 | 4.67 |
| Avg Profit (₹) | 1,78,915 | 87,689 | -24,805 |
| Avg Rainfall (mm) | 852 | 436 | 299 |
| Disease Risk (%) | 54.5 | 40.5 | 38.2 |
| Profitable Farms | 57.8% | 48.9% | 35.5% |

---

*VOIS For Tech / AICTE Data Analytics Internship — Batch 2026-2027*
