from genericpath import isdir
import requests
import re
import os
from PIL import Image
from core.get_basket_id import get_basket_id
import time

def scrap_image(image_link: str, image_folder_path: str):
    response = requests.get(image_link, stream=True)
    image_path = get_new_image_path(image_folder_path, 'webp')

    if not os.path.isdir(image_folder_path):
        os.makedirs(image_folder_path)

    if response.status_code == 200:
        with open(image_path, "xb") as file:
            # use chunks to prevent blocks from service 
            for chunk in response.iter_content(1024):
                file.write(chunk) 
        print(f"The image was successfully saved as {image_path}")
        return image_path
    else:
        print(f"ERROR: {response.status_code}")

def convert_to_png(image_path: str, image_folder_path: str):
    try:
        image = Image.open(image_path)
        new_image_path = get_new_image_path(image_folder_path, 'png')
        image.save(new_image_path)
        os.remove(image_path)
        print(f"The image was successfully converted and saved as {new_image_path}")
        return new_image_path
    except Exception as exception:
        print(f"Convertation Error: {exception}")

def save_image(image_link: str, image_folder_path: str):
    image_path = scrap_image(image_link, image_folder_path)
    new_image_path = convert_to_png(image_path, image_folder_path)
    return new_image_path

def get_new_image_path(image_folder_path: str, file_extension: str):
    image_path = f"{image_folder_path}\\image.{file_extension}"
    time_stamp = time.strftime("%Y%m%d_%H%M%S")
    core, extension = os.path.splitext(image_path)
    return f"{core}_{time_stamp}{extension}"