import os
import pandas as pd

CSV_PATH = r"c:\Users\Admin\Documents\DA301\datasets\mwg_manual_reporting_workflow.csv"

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    source_label = f"FULL_40_ROWS (n={len(df)})"
else:
    source_label = "SAMPLE_8_ROWS (ST_001..ST_008) + CONTROL_TOTALS_40"
    df = pd.DataFrame([
        ("ST_001", "MWG Chi nhanh 1", "Mien Trung", "Laptop", 535.0, 476.0, 95, 3.7),
        ("ST_002", "MWG Chi nhanh 2", "Mien Nam", "Phu kien", 570.0, 530.0, 106, 4.9),
        ("ST_003", "MWG Chi nhanh 3", "Tay Nguyen", "Dien gia dung", 605.0, 586.0, 117, 6.1),
        ("ST_004", "MWG Chi nhanh 4", "Mien Tay", "Dong ho", 640.0, 646.0, 129, 7.3),
        ("ST_005", "MWG Chi nhanh 5", "Mien Bac", "Dien thoai", 675.0, 708.0, 141, 8.5),
        ("ST_006", "MWG Chi nhanh 6", "Mien Trung", "Laptop", 710.0, 660.0, 132, 9.7),
        ("ST_007", "MWG Chi nhanh 7", "Mien Nam", "Phu kien", 745.0, 714.0, 143, 10.9),
        ("ST_008", "MWG Chi nhanh 8", "Tay Nguyen", "Dien gia dung", 780.0, 770.0, 154, 12.1),
    ], columns=["store_id", "store_name", "region", "category", "target_revenue_mil", "actual_revenue_mil", "units_sold", "stockout_rate_pct"])

df["gap_mil"] = df["actual_revenue_mil"] - df["target_revenue_mil"]
cat_summary = df.groupby("category").agg(
    stores=("store_id", "count"),
    target_mil=("target_revenue_mil", "sum"),
    actual_mil=("actual_revenue_mil", "sum"),
    gap_mil=("gap_mil", "sum"),
    units_sold=("units_sold", "sum"),
    avg_stockout_pct=("stockout_rate_pct", "mean"),
).sort_values("gap_mil")
cat_summary["completion_pct"] = (cat_summary["actual_mil"] / cat_summary["target_mil"] * 100).round(2)
cat_summary["avg_stockout_pct"] = cat_summary["avg_stockout_pct"].round(2)

print(f"=== B2A CATEGORY COMPARISON ({source_label}) ===")
print(cat_summary.to_string())
print(f"\nSample Control Total -> Target: {df['target_revenue_mil'].sum():.1f} | Actual: {df['actual_revenue_mil'].sum():.1f} | Gap: {df['gap_mil'].sum():.1f} | Units: {df['units_sold'].sum()}")

