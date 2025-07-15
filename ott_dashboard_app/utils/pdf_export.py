
from fpdf import FPDF
import pandas as pd

def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="OTT Platform Report", ln=True, align='C')
    pdf.ln(10)

    summary = df['platform'].value_counts().reset_index()
    summary.columns = ['Platform', 'Count']
    for _, row in summary.iterrows():
        pdf.cell(200, 10, txt=f"{row['Platform']}: {row['Count']} titles", ln=True)

    pdf.output("OTT_Report.pdf")
