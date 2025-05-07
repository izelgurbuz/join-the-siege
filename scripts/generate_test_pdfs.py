from fpdf import FPDF
import os

os.makedirs('sample_files', exist_ok=True)
samples = {
    "drivers_license_sample.pdf": "Driver's license document",
    "bank_statement_sample.pdf": "Bank statement details",
    "invoice_sample.pdf": "Invoice for purchase",
    "unknown_sample.pdf": "Random unrelated document"
}

for filename, text in samples.items():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(f"sample_files/{filename}")

print("✅ Sample PDFs generated!")
