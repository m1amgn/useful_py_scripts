# pip install gtts pypdf2

import PyPDF2
from gtts import gTTS


def convert_pdf_to_audio(pdf_path, audio_path):
    # Открываем PDF-файл в режиме бинарного чтения
    with open(pdf_path, 'rb') as pdf_file:
        # Создаём объект класса PdfReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''
        # Проходимся по каждой странице в PDF при помощи цикла
        for page_num in range(len(pdf_reader.pages)):
            # Извлекаем текущую страницу
            page = pdf_reader.pages[page_num]
            # Извлекаем текст с текущей страницы и добавляем его к строке 'text'
            text += page.extract_text()
        # Выводим извлеченный текст из PDF
        print(text)

        # Создаём объект класса gTTS для преобразования текста в речь
        tts = gTTS(text=text, lang='ru')
        # Сохраняем итоговый аудиофайл
        tts.save(audio_path)


convert_pdf_to_audio('document.pdf', 'audio.mp3')
