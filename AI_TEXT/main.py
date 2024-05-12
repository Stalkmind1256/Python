import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'

# Загрузите изображение
img = cv2.imread('Trudovaya_knizhka.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Используем режим --psm 3 для автоматического распознавания текста
config = r'--oem 3 --psm 6'

# Получаем данные распознавания с помощью image_to_data()
data = pytesseract.image_to_data(img, lang='rus', config=config, output_type=pytesseract.Output.DICT)
text = pytesseract.image_to_string(img, lang='rus', config=config)
print(data)
print(text)

# Итерируем по обнаруженному тексту
for i, text_data in enumerate(data['text']):
    if text_data.strip():  # Пропускаем пустые строки
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, text_data, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

# Создаем перетаскиваемое окно
window_name = 'Result'
cv2.namedWindow(window_name)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

# Масштабируем изображение для отображения в окне
max_height = 800  # Максимальная высота окна
height, width, _ = img.shape
scale_factor = max_height / height
new_width = int(width * scale_factor)
new_height = int(height * scale_factor)
resized_img = cv2.resize(img, (new_width, new_height))

# Отображаем изображение в перетаскиваемом окне
cv2.imshow(window_name, resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()