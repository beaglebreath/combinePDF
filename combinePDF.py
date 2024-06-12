import os
from PyPDF2 import PdfReader, PdfWriter

def combine_pdfs(directory, output_path):
    writer = PdfWriter()

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            reader = PdfReader(pdf_path)

            for page in reader.pages:
                writer.add_page(page)

    # Save the combined PDF to the output path
    with open(output_path, "wb") as output_pdf_file:
        writer.write(output_pdf_file)

if __name__ == "__main__":
    directory = "."  # Current directory
    output_path = "./Quality_Manual.pdf"  # Output path for the combined PDF
    combine_pdfs(directory, output_path)
