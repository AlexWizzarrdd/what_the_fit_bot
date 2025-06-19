from genericpath import isdir
import requests
import re
import os
from PIL import Image
from core.parser.get_basket_id import get_basket_id
import time
import tempfile

def scrap_image(image_link: str):
    response = requests.get(image_link, stream=True)
    temp_folder = tempfile.gettempdir()
    image_path = get_new_image_path(temp_folder, 'webp')

    if response.status_code == 200:
        with open(image_path, "xb") as file:
            # use chunks to prevent blocks from service 
            for chunk in response.iter_content(1024):
                file.write(chunk) 
        print(f"The image was successfully saved as {image_path}")
        return image_path
    else:
        print(f"ERROR: {response.status_code}")

def convert_to_png(image_path: str):
    try:
        image = Image.open(image_path)
        new_image_path = re.sub("webp", "png", image_path)
        image.save(new_image_path)
        os.remove(image_path)
        print(f"The image was successfully converted and saved as {new_image_path}")
        return new_image_path
    except Exception as exception:
        print(f"Convertation Error: {exception}")

def save_image(image_link: str):
    try:
        image_path = scrap_image(image_link)
        new_image_path = convert_to_png(image_path)
        return new_image_path
    except Exception as exception:
        print(f"Can't save image': {exception}")
    
def get_new_image_path(image_folder_path: str, file_extension: str):
    if not os.path.isdir(image_folder_path):
        raise ValueError("Wrong folder path!")
    if not re.match(r"[a-z]+", file_extension):
        raise ValueError("Wrong folder path!")
    image_path = os.path.join(image_folder_path, f"image.{file_extension}")
    time_stamp = time.strftime("%Y%m%d_%H%M%S")
    core, extension = os.path.splitext(image_path)
    return f"{core}_{time_stamp}{extension}"