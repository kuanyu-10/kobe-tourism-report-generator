from src.load_data import load_tourism_data
from src.analyze_data import add_popularity_score, calculate_kpi, area_analysis, category_analysis, top10_spots
from src.excel_report import create_excel_report
from src.pdf_report import create_pdf_report


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

create_pdf_report(kpi)
print("PDF Report Created")