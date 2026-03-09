from fpdf import FPDF

def generate_cam(company, score, loan):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)
    pdf.cell(200,10,"Credit Appraisal Memo",ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(200,10,f"Company: {company}",ln=True)
    pdf.cell(200,10,f"Risk Score: {score}",ln=True)
    pdf.cell(200,10,f"Recommended Loan: {loan}",ln=True)

    pdf.output("CAM_Report.pdf")
