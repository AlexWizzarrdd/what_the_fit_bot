
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from core.ai.color_and_labels import color_names, label_names
from urllib.request import urlretrieve
import os
from core.parser.image import convert_to_png



def init_model():
    # путь к файлу .keras
    model_url = "https://github.com/AlexWizzarrdd/what_the_fit_bot/raw/master/src/core/ai/cloth_recognition_model.keras"
    local_model_path = "/project/src/core/ai/cloth_recognition_model.keras"
    if not os.path.exists(local_model_path):
        print("Скачивание модели с GitHub...")
    urlretrieve(model_url, local_model_path)
    
    # Загрузка модели
    return tf.keras.models.load_model(local_model_path)

model = init_model()
def analyze_photo(file_path):
    path = convert_to_png(file_path)

    target_size=(224, 224)
    img = image.load_img(path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Обработка изображения
    predictions = model.predict(img_array)
    color_predictions = predictions[1]
    label_predictions = predictions[0]

    # Находим лучший цвет
    best_color_idx = np.argmax(color_predictions)
    best_color_name = color_names[best_color_idx]

    # Находим лучший тип товара
    best_label_idx = np.argmax(label_predictions)
    best_label_name = label_names[best_label_idx]

    print(f"Predicted: {best_label_name} {best_color_name}")

    return f"{best_color_name} {best_label_name}"


"""def load_and_preprocess_image(image):
    # Чтение файла
    
    #img = image.load_img(image_path, target_size=target_size)
    image = tf.io.read_file(image_path)
    
    # Определение типа изображения и декодирование
    if image_path.lower().endswith('.png'):
        image = tf.image.decode_png(image, channels=3)  # PNG
    else:  
        image = tf.image.decode_jpeg(image, channels=3) # JPG
    
    # Конвертация в grayscale
    image = tf.image.rgb_to_grayscale(image)
    
    # Ресайз и нормализация
    image = tf.image.resize(image, [224, 224])
    image = image / 255.0  # Нормализация [0, 1]
    
    # Добавляем batch-размер, необходим для нейронок
    image = tf.expand_dims(image, axis=0)
    
    return image
"""
"""
[label_prefiction, color_prediction] = model.predict(processed_image)

# 1. Загружаем и декодируем изображение
image_path = "\photo\jemper_goluboi.png"
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image, channels=1)  # channels=1 → сразу в grayscale

# 2. Ресайз до 224x224
image = tf.image.resize(image, [224, 224])

# 3. Нормализация (если нужно)
image = image / 255.0  # Приводим к [0, 1]

# 4. Добавляем batch-размер (если нужно для модели)
image = tf.expand_dims(image, axis=0)  # Формат: (1, 224, 224, 1)

print(image.shape)  # Проверка: (1, 224, 224, 1)

#     predicted_color = np.argmax(color_prediction)
#    predicted_label = np.argmax(label_prefiction)
#    predicted_color_class = color_names.get(predicted_color, "Unknown")
#    predicted_label_class = label_names.get(predicted_label, "Unknown")
"""
