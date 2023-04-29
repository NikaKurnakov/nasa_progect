import requests
import os

def get_images(filename, image_list):
    os.makedirs("images", exist_ok=True)
    counter = 0
    for image in image_list:
        filename1 = f"images/{filename}_{counter}.png"
        counter += 1
        response = requests.get(image)
        if response.status_code == 200:
            with open(filename1, 'wb') as file:
                file.write(response.content)