import os
import pdfkit
from concurrent.futures import ThreadPoolExecutor

WKHTMLTOPDF_PATH = r'C:\Users\User\Documents\wkhtmltopdf\bin\wkhtmltopdf.exe'
PDF_OUTPUT_FOLDER = r"C:\Users\User\Desktop\NAJOT TA'LIM\omonimlar"
WEBSITE_URL_TEMPLATE = 'https://tilshunos.com/omonims/?page={}'
MAX_THREADS = 10

def save_website_as_pdf(url, output_path):
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    pdfkit.from_url(url, output_path, configuration=config)

def process_website(index):
    website_url = WEBSITE_URL_TEMPLATE.format(index)
    pdf_output_path = os.path.join(PDF_OUTPUT_FOLDER, f'output{index}.pdf')

    if not os.path.exists(PDF_OUTPUT_FOLDER):
        os.makedirs(PDF_OUTPUT_FOLDER)

    save_website_as_pdf(website_url, pdf_output_path)
    print(f"Web page {index} saved as PDF")

if __name__ == "__main__":
    with ThreadPoolExecutor(MAX_THREADS) as executor:
        executor.map(process_website, range(1, 11))
