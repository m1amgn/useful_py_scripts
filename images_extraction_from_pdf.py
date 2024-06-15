# pip install pymupdf
import fitz


file = 'my_pdf.pdf'

# Открытие PDF-файла
pdf = fitz.open(file)

# Перебор каждой страницы PDF-файла
for i in range(len(pdf)):
    # Перебор каждого изображения на текущей странице
    for image in pdf.get_page_images(i):
        # Получение ссылки на изображение
        xref = image[0]
        # Создание объекта пиксмапы из ссылки на изображение
        pix = fitz.Pixmap(pdf, xref)
        # Проверка, имеет ли изображение менее 5 цветовых компонентов (не является ли изображением в формате CMYK)
        if pix.n < 5:
            # Сохранение пиксмапы в виде изображения PNG
            pix.save(f'{xref}.png')
        else:
            # Создание новой пиксмапы с цветовым пространством RGB
            pix1 = fitz.open(fitz.csRGB, pix)
            # Сохранение новой пиксмапы в виде изображения PNG
            pix1.save(f'{xref}.png')
            # Освобождение ресурсов, связанных с новой пиксмапой
            pix1 = None
        # Освобождение ресурсов, связанных с исходной пиксмапой
        pix = None