import requests
import argparse
import load_image
from datetime import datetime


def get_epic_picture(args):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
    params = {
        'api_key': args.token_epic
    }
    response = requests.get(epic_url, params=params)
    unpacked_response = response.json()
    epic_images = []
    images_number = int(args.numb)
    for image in range(images_number):
        image_name = unpacked_response[image]['image']
        image_date_json = unpacked_response[image]['date']
        if image_name and image_date_json:
            image_date_format = datetime.fromisoformat(image_date_json)
            image_date = datetime.date(image_date_format).strftime("%Y/%m/%d")
            epic_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"
            epic_images.append(epic_image_url)
    return epic_images

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token_epic", help="token epic", required=True)
    parser.add_argument("--numb", help="numb picture")
    args = parser.parse_args()
    epic_function = get_epic_picture(epic_url, args)
    load_image.get_images("epic_image", epic_function, parser)


if __name__ == '__main__':
    main()
