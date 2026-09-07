import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print('========================================================')
    print(' Seasonal Agriculture Performance Analysis — Pipeline')
    print('========================================================')
    
    # 1. Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'seasonal_agriculture_performance_dataset.csv')
    charts_dir = os.path.join(base_dir, 'charts')
    os.makedirs(charts_dir, exist_ok=True)
    
    if not os.path.exists(data_path):
        print(f'Error: Dataset not found at {data_path}')
        sys.exit(1)
        
    # 2. Load Data
    print(f'Loading dataset from {data_path}...')
    df = pd.read_csv(data_path)
    print(f'Dataset loaded successfully: {df.shape[0]:,} rows × {df.shape[1]} columns')
    
    # 3. Data Cleaning
    missing_before = df.isnull().sum().sum()
    print(f'Missing values before cleaning: {missing_before}')
    
    clean_cols = ['Rainfall_mm', 'Soil_Moisture_pct', 'Yield_Tonnes_Ha']
    for col in clean_cols:
        if col in df.columns:
            cnt = df[col].isnull().sum()
            if cnt > 0:
                med = df[col].median()
                df[col] = df[col].fillna(med)
                print(f'  - Imputed {cnt} missing values in \'{col}\' with median = {med}')
                
    missing_after = df.isnull().sum().sum()
    print(f'Missing values after cleaning: {missing_after}')
    assert missing_after == 0, 'Missing values remain after cleaning!'
    
    # 4. Generate Visualizations
    print('\nGenerating 12 analytical charts...')
    palette_seasons = ['#2E86AB', '#A23B72', '#F18F01'] # Kharif, Rabi, Zaid
    palette_irrigation = ['#264653', '#2A9D8F', '#E9C46A', '#E76F51']
    
    # Chart 1: Average Yield by Season
    season_yield = df.groupby('Season')['Yield_Tonnes_Ha'].agg(['mean', 'median', 'std']).round(2)
    season_yield.columns = ['Mean Yield (t/ha)', 'Median Yield (t/ha)', 'Std Dev']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(season_yield.index, season_yield['Mean Yield (t/ha)'], color=palette_seasons, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Yield by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Yield (Tonnes/Hectare)')
    for bar, val in zip(bars, season_yield['Mean Yield (t/ha)']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{val}', ha='center', fontsize=11)
    plt.tight_layout()
    p1 = os.path.join(charts_dir, '01_avg_yield_by_season.png')
    plt.savefig(p1, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 01_avg_yield_by_season.png')

    # Chart 2: Average Profit by Season
    season_profit = df.groupby('Season')['Profit_INR'].agg(['mean', 'median']).round(2)
    season_profit.columns = ['Mean Profit (₹)', 'Median Profit (₹)']
    fig, ax = plt.subplots(figsize=(8, 5))
    profit_vals = season_profit['Mean Profit (₹)']
    bar_colors = ['#2E86AB' if v >= 0 else '#E63946' for v in profit_vals]
    bars = ax.bar(profit_vals.index, profit_vals.values, color=bar_colors, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Profit by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Profit (₹)')
    ax.axhline(y=0, color='black', linewidth=0.8, linestyle='--')
    for bar, val in zip(bars, profit_vals.values):
        ypos = bar.get_height() + 3000 if val >= 0 else bar.get_height() - 12000
        ax.text(bar.get_x() + bar.get_width()/2, ypos, f'₹{val:,.0f}', ha='center', fontsize=10)
    plt.tight_layout()
    p2 = os.path.join(charts_dir, '02_avg_profit_by_season.png')
    plt.savefig(p2, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 02_avg_profit_by_season.png')

    # Chart 3: Total Production by Season
    season_prod = df.groupby('Season')['Production_Tonnes'].agg(['sum', 'mean']).round(2)
    season_prod.columns = ['Total Production (Tonnes)', 'Mean Production (Tonnes)']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(season_prod.index, season_prod['Total Production (Tonnes)'], color=palette_seasons, edgecolor='black', linewidth=0.5)
    ax.set_title('Total Production by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Production (Tonnes)')
    for bar, val in zip(bars, season_prod['Total Production (Tonnes)']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500, f'{val:,.0f}', ha='center', fontsize=10)
    plt.tight_layout()
    p3 = os.path.join(charts_dir, '03_total_production_by_season.png')
    plt.savefig(p3, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 03_total_production_by_season.png')

    # Chart 4: Rainfall vs Yield (scatter)
    fig, ax = plt.subplots(figsize=(10, 6))
    season_colors_map = {'Kharif': '#2E86AB', 'Rabi': '#A23B72', 'Zaid': '#F18F01'}
    for s, color in season_colors_map.items():
        mask = df['Season'] == s
        ax.scatter(df.loc[mask, 'Rainfall_mm'], df.loc[mask, 'Yield_Tonnes_Ha'], alpha=0.3, s=15, color=color, label=s)
    ax.set_title('Rainfall vs Yield', fontweight='bold', pad=15)
    ax.set_xlabel('Rainfall (mm)')
    ax.set_ylabel('Yield (Tonnes/Hectare)')
    ax.legend(title='Season')
    plt.tight_layout()
    p4 = os.path.join(charts_dir, '04_rainfall_vs_yield.png')
    plt.savefig(p4, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 04_rainfall_vs_yield.png')

    # Chart 5: Temperature vs Yield
    fig, ax = plt.subplots(figsize=(10, 6))
    for s, color in season_colors_map.items():
        mask = df['Season'] == s
        ax.scatter(df.loc[mask, 'Avg_Temperature_C'], df.loc[mask, 'Yield_Tonnes_Ha'], alpha=0.3, s=15, color=color, label=s)
    ax.set_title('Temperature vs Yield', fontweight='bold', pad=15)
    ax.set_xlabel('Average Temperature (°C)')
    ax.set_ylabel('Yield (Tonnes/Hectare)')
    ax.legend(title='Season')
    plt.tight_layout()
    p5 = os.path.join(charts_dir, '05_temperature_vs_yield.png')
    plt.savefig(p5, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 05_temperature_vs_yield.png')

    # Chart 6: Water Usage by Season
    water_season = df.groupby('Season')['Water_Used_m3'].agg(['mean', 'median']).round(2)
    water_season.columns = ['Mean Water Used (m³)', 'Median Water Used (m³)']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(water_season.index, water_season['Mean Water Used (m³)'], color=palette_seasons, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Water Usage by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Water Used (m³)')
    for bar, val in zip(bars, water_season['Mean Water Used (m³)']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, f'{val:,.0f}', ha='center', fontsize=11)
    plt.tight_layout()
    p6 = os.path.join(charts_dir, '06_water_usage_by_season.png')
    plt.savefig(p6, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 06_water_usage_by_season.png')

    # Chart 7: Water Efficiency by Season
    water_eff_season = df.groupby('Season')['Water_Efficiency_t_per_1000m3'].agg(['mean', 'median']).round(2)
    water_eff_season.columns = ['Mean Water Efficiency', 'Median Water Efficiency']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(water_eff_season.index, water_eff_season['Mean Water Efficiency'], color=palette_seasons, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Water Efficiency by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Water Efficiency (t per 1000 m³)')
    for bar, val in zip(bars, water_eff_season['Mean Water Efficiency']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f'{val}', ha='center', fontsize=11)
    plt.tight_layout()
    p7 = os.path.join(charts_dir, '07_water_efficiency_by_season.png')
    plt.savefig(p7, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 07_water_efficiency_by_season.png')

    # Chart 8: Disease/Pest Risk by Season
    disease_season = df.groupby('Season')['Disease_Pest_Risk_pct'].agg(['mean', 'median']).round(2)
    disease_season.columns = ['Mean Disease Risk (%)', 'Median Disease Risk (%)']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(disease_season.index, disease_season['Mean Disease Risk (%)'], color=palette_seasons, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Disease/Pest Risk by Season', fontweight='bold', pad=15)
    ax.set_xlabel('Season')
    ax.set_ylabel('Disease/Pest Risk (%)')
    for bar, val in zip(bars, disease_season['Mean Disease Risk (%)']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{val}%', ha='center', fontsize=11)
    plt.tight_layout()
    p8 = os.path.join(charts_dir, '08_disease_risk_by_season.png')
    plt.savefig(p8, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 08_disease_risk_by_season.png')

    # Chart 9: Crop-wise Average Yield
    crop_yield = df.groupby('Crop')['Yield_Tonnes_Ha'].agg(['mean', 'median', 'count']).round(2)
    crop_yield.columns = ['Mean Yield (t/ha)', 'Median Yield (t/ha)', 'Count']
    crop_yield = crop_yield.sort_values('Mean Yield (t/ha)', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    crop_colors = ['#264653', '#2A9D8F', '#E9C46A', '#F4A261', '#E76F51', '#606C38', '#283618', '#DDA15E']
    bars = ax.barh(crop_yield.index[::-1], crop_yield['Mean Yield (t/ha)'][::-1], color=crop_colors[:len(crop_yield)], edgecolor='black', linewidth=0.5)
    ax.set_title('Crop-wise Average Yield', fontweight='bold', pad=15)
    ax.set_xlabel('Average Yield (Tonnes/Hectare)')
    for bar, val in zip(bars, crop_yield['Mean Yield (t/ha)'][::-1]):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, f'{val}', va='center', fontsize=10)
    plt.tight_layout()
    p9 = os.path.join(charts_dir, '09_crop_wise_avg_yield.png')
    plt.savefig(p9, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 09_crop_wise_avg_yield.png')

    # Chart 10: Irrigation Method vs Yield
    irr_yield = df.groupby('Irrigation_Method')['Yield_Tonnes_Ha'].agg(['mean', 'median', 'count']).round(2)
    irr_yield.columns = ['Mean Yield', 'Median Yield', 'Count']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(irr_yield.index, irr_yield['Mean Yield'], color=palette_irrigation, edgecolor='black', linewidth=0.5)
    ax.set_title('Average Yield by Irrigation Method', fontweight='bold', pad=15)
    ax.set_xlabel('Irrigation Method')
    ax.set_ylabel('Average Yield (Tonnes/Hectare)')
    for bar, val in zip(bars, irr_yield['Mean Yield']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{val}', ha='center', fontsize=11)
    plt.tight_layout()
    p10 = os.path.join(charts_dir, '10_irrigation_vs_yield.png')
    plt.savefig(p10, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 10_irrigation_vs_yield.png')

    # Chart 11: Irrigation Method vs Water Efficiency
    irr_water_eff = df.groupby('Irrigation_Method')['Water_Efficiency_t_per_1000m3'].agg(['mean', 'median']).round(2)
    irr_water_eff.columns = ['Mean Water Efficiency', 'Median Water Efficiency']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(irr_water_eff.index, irr_water_eff['Mean Water Efficiency'], color=palette_irrigation, edgecolor='black', linewidth=0.5)
    ax.set_title('Water Efficiency by Irrigation Method', fontweight='bold', pad=15)
    ax.set_xlabel('Irrigation Method')
    ax.set_ylabel('Water Efficiency (t per 1000 m³)')
    for bar, val in zip(bars, irr_water_eff['Mean Water Efficiency']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f'{val}', ha='center', fontsize=11)
    plt.tight_layout()
    p11 = os.path.join(charts_dir, '11_irrigation_vs_water_efficiency.png')
    plt.savefig(p11, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 11_irrigation_vs_water_efficiency.png')

    # Chart 12: Correlation Heatmap
    corr_cols = ['Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 'Soil_pH', 
                 'Soil_Moisture_pct', 'Fertilizer_kg_ha', 'Yield_Tonnes_Ha', 
                 'Production_Tonnes', 'Profit_INR', 'Water_Used_m3', 
                 'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct']
    corr_matrix = df[corr_cols].corr().round(3)
    fig, ax = plt.subplots(figsize=(12, 10))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r', 
                center=0, vmin=-1, vmax=1, square=True, linewidths=0.5,
                cbar_kws={'shrink': 0.8}, ax=ax, annot_kws={'size': 8})
    ax.set_title('Correlation Heatmap — Key Agricultural Variables', fontweight='bold', pad=20)
    plt.tight_layout()
    p12 = os.path.join(charts_dir, '12_correlation_heatmap.png')
    plt.savefig(p12, dpi=150, bbox_inches='tight')
    plt.close()
    print('  [✓] 12_correlation_heatmap.png')
    
    # 5. Verification
    print('\nVerifying generated charts...')
    all_ok = True
    for i in range(1, 13):
        # find matching file
        fname = [f for f in os.listdir(charts_dir) if f.startswith(f'{i:02d}_')]
        if not fname:
            print(f'  [✗] Missing chart for index {i:02d}')
            all_ok = False
        else:
            fpath = os.path.join(charts_dir, fname[0])
            sz = os.path.getsize(fpath)
            if sz == 0:
                print(f'  [✗] Empty file: {fname[0]}')
                all_ok = False
            else:
                print(f'  [✓] {fname[0]} ({sz:,} bytes)')
                
    if not all_ok:
        print('\nPipeline failed chart verification!')
        sys.exit(1)
        
    print('\n========================================================')
    print(' Pipeline successfully executed! All 12 charts generated.')
    print('========================================================')

if __name__ == '__main__':
    main()
