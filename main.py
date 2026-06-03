from src.load_data import load_tourism_data
from src.analyze_data import add_popularity_score, calculate_kpi, area_analysis, category_analysis, top10_spots
from src.excel_report import create_excel_report

file_path = "data/kobe_tourism_spots.xlsx"

df = load_tourism_data(file_path)

df = add_popularity_score(df)

kpi = calculate_kpi(df)

area_df = area_analysis(df)

category_df = category_analysis(df)

top10_df = top10_spots(df)

create_excel_report(
    kpi,
    area_df,
    category_df,
    top10_df
)

print("\n=== KPI ===")
print(f"総スポット数: {kpi['total_spots']}")
print(f"平均評価: {kpi['average_rating']}")
print(f"総レビュー数: {kpi['total_reviews']}")
print(f"人気スポット: {kpi['top_spot']}")
print(f"Popularity Score: {kpi['top_score']}")
print("\n=== Area Analysis ===")
print(area_df)
print("\n=== Category Analysis ===")
print(category_df)
print("\n=== Top10 Spots ===")
print(top10_df)
print("\nExcel Report Created")