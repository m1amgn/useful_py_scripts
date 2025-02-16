from pathlib import Path
from PyPDF2 import PdfMerger


def merge_pdfs_in_directory(directory_path, output_path):
    merger = PdfMerger()

    for file_path in Path(directory_path).rglob('*.pdf'):
        merger.append(file_path)

    merger.write(output_path)
    merger.close()


directory_path = ''
output_path = ''

merge_pdfs_in_directory(directory_path, output_path)
