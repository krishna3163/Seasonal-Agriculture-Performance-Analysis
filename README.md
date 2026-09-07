# Seasonal Agriculture Performance Analysis

[![Automated Agriculture Analysis & Chart Generation](https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis/actions/workflows/generate_charts.yml/badge.svg)](https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis/actions/workflows/generate_charts.yml)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end applied Data Analytics project investigating seasonal variations in agricultural productivity, resource utilization, environmental linkages, and economic profitability across **4,000 farm records** in India.

**Internship:** VOIS For Tech / AICTE Data Analytics Internship (Batch 2026–2027)  
**Student Name:** Krishna Kumar  
**College Name:** Ambalika Institute of Management and Technology, Lucknow  
**AICTE STU ID:** STU6a252b77248381780820855  

---

## 📌 Project Overview

Agricultural activities in India are heavily contingent on seasonal weather patterns, resource availability, and soil dynamics. This project analyzes agricultural performance across three primary cropping seasons—**Kharif (Monsoon)**, **Rabi (Winter)**, and **Zaid (Summer)**—covering 8 crops, 8 states, 10 districts, and 4 irrigation methods.

### Key Objectives:
1. **Seasonal Productivity Comparison:** Quantify yield, production volume, and net financial returns across seasons.
2. **Irrigation & Water Efficiency:** Assess water consumption and productivity across Drip, Flood, Rainfed, and Sprinkler systems.
3. **Climate & Disease Vulnerability:** Model the correlation between environmental factors (precipitation, humidity, heat) and pest/disease outbreak risk.
4. **Automated CI/CD Analytics:** Provide an automated Python pipeline and GitHub Actions workflow for full analytical reproducibility.

---

## 📊 Summary of Key Findings

| Metric | Kharif (Monsoon) | Rabi (Winter) | Zaid (Summer) | Benchmark / Dominant Driver |
|---|---|---|---|---|
| **Average Yield (t/ha)** | **5.63** | **5.04** | **4.64** | Kharif achieves highest yield due to monsoon precipitation |
| **Average Profit (₹)** | **₹1,78,915** | **₹87,689** | **-₹24,805** | Zaid experiences net negative average profitability |
| **Profitable Farms (%)** | **57.8%** | **48.9%** | **35.5%** | Only 35.5% of summer farms generate positive returns |
| **Total Production (t)** | **82,388 t** | **67,499 t** | **23,098 t** | Kharif represents 47.6% of overall output volume |
| **Average Rainfall (mm)** | **849 mm** | **438 mm** | **305 mm** | Severe moisture deficits during summer cultivation |
| **Disease & Pest Risk (%)** | **54.5%** | **40.5%** | **38.2%** | Moderate-to-strong correlation with rainfall ($r = 0.622$) |
| **Top Irrigation Method** | Drip ($6.58$ t/ha) | Drip ($6.58$ t/ha) | Drip ($6.58$ t/ha) | Drip yields 43% higher output than rainfed farming |

---

## 📁 Repository Structure

```
Seasonal-Agriculture-Performance-Analysis/
│
├── .github/workflows/
│   └── generate_charts.yml                         # GitHub Actions CI/CD automated analysis workflow
│
├── charts/                                         # 12 Publication-quality analytical visualizations (PNG)
│   ├── 01_avg_yield_by_season.png                  # Season-wise average crop yield
│   ├── 02_avg_profit_by_season.png                 # Season-wise net financial profitability
│   ├── 03_total_production_by_season.png           # Aggregate harvest production volume
│   ├── 04_rainfall_vs_yield.png                    # Bivariate scatter: precipitation vs yield
│   ├── 05_temperature_vs_yield.png                 # Bivariate scatter: thermal conditions vs yield
│   ├── 06_water_usage_by_season.png                # Seasonal water consumption ($m^3$)
│   ├── 07_water_efficiency_by_season.png           # Water productivity ($t / 1000m^3$)
│   ├── 08_disease_risk_by_season.png               # Pest and crop disease vulnerability
│   ├── 09_crop_wise_avg_yield.png                  # Comparative crop yields across 8 varieties
│   ├── 10_irrigation_vs_yield.png                  # Yield performance by irrigation technique
│   ├── 11_irrigation_vs_water_efficiency.png       # Irrigation technique water productivity
│   └── 12_correlation_heatmap.png                  # Full Pearson correlation matrix (28 features)
│
├── generate_charts.py                              # Automated Python script to clean data & regenerate figures
├── requirements.txt                                # Pinned Python dependencies
├── seasonal_agriculture_performance_dataset.csv    # Benchmark dataset: 4,000 records × 28 features
├── Seasonal_Agriculture_Performance_Analysis.ipynb # Complete Jupyter Notebook (85 cells, executed outputs)
├── VOIS_Project_PPT.pptx                           # Professional 14-slide Major Project Presentation
└── README.md                                       # Project documentation
```

---

## ⚙️ Automated GitHub Actions Workflow

This repository includes a fully automated **GitHub Actions CI/CD pipeline** ([`.github/workflows/generate_charts.yml`](.github/workflows/generate_charts.yml)):

1. **Automatic Trigger:** Runs on every push or pull request to `main`, and can also be manually triggered via `workflow_dispatch`.
2. **Environment Setup:** Spins up an Ubuntu runner, configures Python 3.11, and caches pip dependencies.
3. **Data Integrity Audit:** Programmatically validates dataset dimensions ($4,000 \times 28$) and column schema.
4. **Autonomous Chart Generation:** Executes [`generate_charts.py`](generate_charts.py) to clean data and regenerate all 12 figures.
5. **Artifact Publishing:** Automatically packages all generated charts as a downloadable build artifact for verification.

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis.git
cd Seasonal-Agriculture-Performance-Analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Analysis & Charts Automatically
```bash
python generate_charts.py
```
*All 12 charts will be automatically regenerated and saved into the `charts/` folder with complete execution logs.*

### 4. Open the Jupyter Notebook
```bash
jupyter notebook Seasonal_Agriculture_Performance_Analysis.ipynb
```

---

## 🛠️ Technology Stack

- **Runtime & Environment:** Python 3.11+, Jupyter Notebook
- **Data Wrangling:** Pandas, NumPy
- **Visualizations:** Matplotlib, Seaborn
- **Automation & CI/CD:** GitHub Actions
- **Presentation:** Microsoft PowerPoint (python-pptx)

---

## 👨‍🎓 Project Credits & Ownership

- **Student:** Krishna Kumar  
- **Institute:** Ambalika Institute of Management and Technology, Lucknow  
- **Internship:** VOIS For Tech / AICTE Data Analytics Internship (Batch 2026–2027)  
- **Certification:** VOIS LMS Course Completion in Data Visualization (`VFLMS26_163451`)
