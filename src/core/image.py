import requests
import re
import os
from PIL import Image
from core.get_basket_id import get_basket_id

def scrap_image(image_link: str, image_folder_path: str):
    response = requests.get(image_link, stream=True)
    image_path = f"{image_folder_path}\\image.webp"
    os.makedirs(image_folder_path)

    if response.status_code == 200:
        # make and open an image file
        with open(image_path, "xb") as file:
            # write info chunkes down in the file
            for chunk in response.iter_content(1024):
                file.write(chunk) 
        print(f"The image was successfully saved as {image_path}")
        return image_path
    else:
        print(f"ERROR: {response.status_code}")

def convert_to_png(image_path: str, image_folder_path: str):
    try:
        image = Image.open(image_path)
        new_image_path = f"{image_folder_path}\\image.png"
        image.save(new_image_path)
        os.remove(image_path)
        print(f"The image was successfully converted and saved as {new_image_path}")
        return new_image_path
    except Exception as exception:
        print(f"Convertation Error: {exception}")