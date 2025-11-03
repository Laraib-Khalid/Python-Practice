from PyPDF2 import PdfMerger

# Create merger object
merger = PdfMerger()

# List of PDFs to merge
pdf_files = ["Cheatsheet.pdf", "Cheatsheet.pdf", "Cheatsheet.pdf"]

for pdf in pdf_files:
    merger.append(pdf)   # add each PDF file

# Write merged PDF to output
merger.write("merged_output.pdf")
merger.close()

print("✅ PDF files merged successfully!")
