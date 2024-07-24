# pip install opencv-python mediapipe numpy

import cv2
import mediapipe as mp
import numpy as np

# Инициализация Mediapipe Selfie Segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation

# Загрузка изображения
image_path = 'image.png'
image = cv2.imread(image_path)
height, width, _ = image.shape

# Создание копии изображения для размывания фона
blurred_image = cv2.GaussianBlur(image, (21, 21), 0)

# Инициализация Selfie Segmentation
with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
    # Обработка изображения
    results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Создание маски для области человека
    mask = results.segmentation_mask > 0.5
    mask = mask.astype(np.uint8) * 255

    # Инвертирование маски для фона
    background_mask = cv2.bitwise_not(mask)

    # Извлечение фона и размывание его
    background_blurred = cv2.bitwise_and(blurred_image, blurred_image, mask=background_mask)

    # Извлечение человека из исходного изображения
    person = cv2.bitwise_and(image, image, mask=mask)

    # Объединение размытого фона и человека
    final_image = cv2.add(background_blurred, person)

# Сохранение результата
output_path = 'output.jpg'
cv2.imwrite(output_path, final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
