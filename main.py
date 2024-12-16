from PIL import Image, ImageDraw, ImageFont
import os

# Указываем путь к шрифту (проверьте, что путь к шрифту правильный)
font_path = "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"  # Путь к шрифту, на Fedora
font_size = 100  # Размер шрифта

# Директория для сохранения картинок с английскими буквами
output_dir = "generated_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Буквы для генерации
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Генерация картинок с английскими буквами
for letter in letters:
    # Создаем изображение размером 200x200 пикселей с белым фоном
    img = Image.new("RGB", (200, 200), color="white")
    draw = ImageDraw.Draw(img)

    # Используем шрифт и размер шрифта
    font = ImageFont.truetype(font_path, font_size)

    # Получаем размеры текста с помощью textbbox
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Позиционируем текст по центру
    position = ((200 - text_width) / 2, (200 - text_height) / 2)

    # Рисуем текст на изображении
    draw.text(position, letter, font=font, fill="black")

    # Сохраняем картинку
    img.save(os.path.join(output_dir, f"{letter}.png"))

print("Генерация завершена. Картинки с английскими буквами сохранены в папку 'generated_images'.")

# Директория для сохранения картинок с русскими буквами
russian_output_dir = "generated_images_russian"
if not os.path.exists(russian_output_dir):
    os.makedirs(russian_output_dir)

# Русские буквы для генерации
russian_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Генерация картинок с русскими буквами
for letter in russian_letters:
    # Создаем изображение размером 200x200 пикселей с белым фоном
    img = Image.new("RGB", (200, 200), color="white")
    draw = ImageDraw.Draw(img)

    # Используем шрифт и размер шрифта
    font = ImageFont.truetype(font_path, font_size)

    # Получаем размеры текста с помощью textbbox
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Позиционируем текст по центру
    position = ((200 - text_width) / 2, (200 - text_height) / 2)

    # Рисуем текст на изображении
    draw.text(position, letter, font=font, fill="black")

    # Сохраняем картинку
    img.save(os.path.join(russian_output_dir, f"{letter}.png"))

print("Генерация завершена. Картинки с русскими буквами сохранены в папку 'generated_images_russian'.")
