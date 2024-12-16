import cv2
import pytesseract
import os
import re

# Укажите путь к исполняемому файлу tesseract (если нужно, например, на Fedora путь может быть другим)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Функция для обработки и распознавания текста с изображения
def recognize_text(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)

    # Преобразуем изображение в оттенки серого для лучшей обработки
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем фильтрацию для устранения шума
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Увеличиваем контраст
    contrast_image = cv2.equalizeHist(blurred_image)

    # Применяем бинаризацию для улучшения контраста
    _, thresholded_image = cv2.threshold(contrast_image, 150, 255, cv2.THRESH_BINARY)

    # Применяем морфологические операции для улучшения качества изображения
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

    # Используем Tesseract для распознавания текста (указываем языки и настройки для улучшения распознавания)
    config = '--psm 8 --oem 3'  # Режим для распознавания одиночных символов
    text = pytesseract.image_to_string(morph_image, lang='rus', config=config)

    # Очищаем результат и удаляем нежелательные символы
    text = text.strip()
    text = re.sub(r'[^А-Яа-яЁё]', '', text)  # Удаляем все, кроме русских букв

    return text

# Функция для обработки всех изображений в папке
def process_all_images_in_folder(folder_path):
    # Получаем все файлы в папке
    files = os.listdir(folder_path)

    # Фильтруем только изображения
    image_files = [f for f in files if f.endswith('.png')]

    # Обрабатываем все изображения
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        recognized_text = recognize_text(image_path)
        print(f"Распознанный текст с изображения {image_file}: {recognized_text}")

# Начало программы
if __name__ == "__main__":
    # Папка с изображениями букв
    images_folder = 'generated_images_russian'  # Папка с изображениями (измените на вашу папку)

    # Вопрос пользователю
    user_input = input("Хотите обработать все изображения из папки? (да/нет): ").strip().lower()

    if user_input == "да":
        process_all_images_in_folder(images_folder)
        print("Распознавание завершено.")