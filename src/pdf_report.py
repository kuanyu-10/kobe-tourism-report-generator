from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from textwrap import wrap


def draw_page_header(c):
    c.setFont("HeiseiKakuGo-W5", 18)
    c.drawCentredString(297.5, 800, "神戸観光レポート")
    c.line(50, 785, 545, 785)

def draw_page_footer(c, page_number):
    c.setFont("HeiseiKakuGo-W5", 9)
    c.drawCentredString(297.5, 30, f"{page_number} ページ")

def split_text(text):

    lines = []

    sentences = text.strip().split("。")

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:

            wrapped_lines = wrap(
                sentence + "。",
                width=40
            )

            lines.extend(wrapped_lines)

    return lines

def create_pdf_report(
    kpi,
    top10_df,
    area_df,
    category_df,
    ai_summary
):
    file_path = "output/kobe_tourism_report.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)

    pdfmetrics.registerFont(
        UnicodeCIDFont("HeiseiKakuGo-W5")
    )

    # Page 1
    draw_page_header(c)

    c.setFont("HeiseiKakuGo-W5", 12)
    c.drawString(50, 760, "サマリー")

    summary_lines = split_text(ai_summary)

    y = 735

    for line in summary_lines:
        c.drawString(50, y, line)
        y -= 20

    y -= 25

    c.setFont("HeiseiKakuGo-W5", 14)
    c.drawString(50, y, "KPI サマリー")

    y -= 30

    c.setFont("HeiseiKakuGo-W5", 12)

    kpi_items = [
        ("総スポット数", kpi["total_spots"]),
        ("平均評価", kpi["average_rating"]),
        ("総レビュー数", kpi["total_reviews"]),
        ("人気スポット", kpi["top_spot"]),
        ("人気指数", kpi["top_score"])
    ]

    for label, value in kpi_items:
        c.drawString(70, y, f"{label}: {value}")
        y -= 25

    draw_page_footer(c, 1)

    # Page 2
    c.showPage()
    draw_page_header(c)

    y = 750

    c.setFont("HeiseiKakuGo-W5", 14)
    c.drawString(50, y, "人気スポット TOP10")

    y -= 25

    c.setFont("HeiseiKakuGo-W5", 10)

    c.drawString(50, y, "順位")
    c.drawString(90, y, "スポット名")
    c.drawString(280, y, "エリア")
    c.drawString(350, y, "カテゴリ")
    c.drawString(430, y, "評価")
    c.drawString(480, y, "人気指数")
    c.line(50, y - 5, 545, y - 5)

    y -= 20

    for rank, (_, row) in enumerate(
        top10_df.iterrows(),
        start=1
    ):
        c.drawString(50, y, str(rank))
        c.drawString(90, y, str(row["spot_name"]))
        c.drawString(280, y, str(row["area"]))
        c.drawString(350, y, str(row["category"]))
        c.drawString(430, y, str(row["rating"]))
        c.drawString(480, y, str(row["popularity_score"]))

        c.line(50, y - 5, 545, y - 5)

        y -= 20

    y -= 30

    c.setFont("HeiseiKakuGo-W5", 14)
    c.drawString(50, y, "エリア分析")

    y -= 30

    c.setFont("HeiseiKakuGo-W5", 10)

    c.drawString(50, y, "エリア")
    c.drawString(150, y, "スポット数")
    c.drawString(250, y, "平均評価")
    c.drawString(350, y, "総レビュー数")
    c.line(50, y - 5, 500, y - 5)

    y -= 25

    for _, row in area_df.iterrows():
        c.drawString(50, y, str(row["area"]))
        c.drawString(150, y, str(row["spot_count"]))
        c.drawString(250, y, str(row["avg_rating"]))
        c.drawString(350, y, str(row["total_reviews"]))

        y -= 20

    draw_page_footer(c, 2)

    c.showPage()

    draw_page_header(c)

    y = 750

    c.setFont("HeiseiKakuGo-W5", 14)

    c.drawString(50, y, "カテゴリ分析")

    y -= 30

    c.setFont("HeiseiKakuGo-W5", 10)

    c.drawString(50, y, "カテゴリ")
    c.drawString(150, y, "スポット数")
    c.drawString(250, y, "平均評価")
    c.drawString(350, y, "総レビュー数")
    c.drawString(450, y, "平均人気指数")

    c.line(50, y - 5, 545, y - 5)

    y -= 25

    for _, row in category_df.iterrows():

        c.drawString(50, y, str(row["category"]))
        c.drawString(150, y, str(row["spot_count"]))
        c.drawString(250, y, str(row["avg_rating"]))
        c.drawString(350, y, str(row["total_reviews"]))
        c.drawString(450, y, str(row["avg_popularity_score"]))

        c.line(50, y - 5, 545, y - 5)

        y -= 20

    draw_page_footer(c, 3)

    c.save()