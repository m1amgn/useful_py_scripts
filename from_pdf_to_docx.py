# pip install pdfplumber python-docx
import pdfplumber
from docx import Document

# Открываем PDF-файл
pdf = pdfplumber.open("my_pdf.pdf")

# Создаем новый документ Word
doc = Document()

# Проходим по каждой странице в PDF
for page in pdf.pages:
    # Извлекаем текст со страницы
    text = page.extract_text()
    # Добавляем текст в качестве абзаца в документ Word
    doc.add_paragraph(text)

# Сохраняем документ Word
doc.save("output.docx")
