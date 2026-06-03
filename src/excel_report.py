from openpyxl import Workbook


def create_excel_report(
    kpi,
    area_df,
    category_df,
    top10_df
):

    wb = Workbook()

    ws = wb.active
    ws.title = "KPI Summary"

    ws["A1"] = "KPI"
    ws["B1"] = "Value"

    ws["A2"] = "総スポット数"
    ws["B2"] = kpi["total_spots"]

    ws["A3"] = "平均評価"
    ws["B3"] = kpi["average_rating"]

    ws["A4"] = "総レビュー数"
    ws["B4"] = kpi["total_reviews"]

    ws["A5"] = "人気スポット"
    ws["B5"] = kpi["top_spot"]

    # Area Analysis Sheet
    area_ws = wb.create_sheet("Area Analysis")

    area_ws.append([
        "エリア",
        "スポット数",
        "平均評価",
        "総レビュー数"
    ])

    for _, row in area_df.iterrows():
        area_ws.append([
            row["area"],
            row["spot_count"],
            row["avg_rating"],
            row["total_reviews"]
        ])

    category_ws = wb.create_sheet("Category Analysis")

    category_ws.append([
        "カテゴリ",
        "スポット数",
        "平均評価",
        "総レビュー数",
        "平均Popularity Score"
    ])

    for _, row in category_df.iterrows():

        category_ws.append([
            row["category"],
            row["spot_count"],
            row["avg_rating"],
            row["total_reviews"],
            row["avg_popularity_score"]
        ])


        # Top10 Ranking Sheet
    top10_ws = wb.create_sheet("Top10 Ranking")

    top10_ws.append([
        "順位",
        "スポット名",
        "エリア",
        "カテゴリ",
        "評価",
        "レビュー数",
        "Popularity Score"
    ])


    for rank, (_, row) in enumerate(
            top10_df.iterrows(),
            start=1
            ):

        top10_ws.append([
            rank,
            row["spot_name"],
            row["area"],
            row["category"],
            row["rating"],
            row["review_count"],
            row["popularity_score"]
        ])

    wb.save(
        "output/kobe_tourism_report.xlsx"
    )