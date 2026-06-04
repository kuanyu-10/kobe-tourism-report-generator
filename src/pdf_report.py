from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def create_pdf_report(kpi):

    file_path = "output/kobe_tourism_report.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)

    c.drawString(50, 800, "Kobe Tourism Report")
    c.drawString(50, 760, f"Total Spots: {kpi['total_spots']}")
    c.drawString(50, 740, f"Average Rating: {kpi['average_rating']}")
    c.drawString(50, 720, f"Total Reviews: {kpi['total_reviews']}")
    c.drawString(50, 700, f"Top Spot: {kpi['top_spot']}")
    c.drawString(50, 680, f"Popularity Score: {kpi['top_score']}")

    c.save()