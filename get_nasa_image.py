import requests
import json
import argparse
import load_image


def get_nasa_apod_picture(nasa_url, args):
    params = {
        'start_date': "2023-03-15",
        'end_date': "2023-04-15",
        'api_key': args.token_nasa
    }
    response = requests.get(nasa_url, params=params)
    picture_today = response.json()
    date_pictures = json.dumps(picture_today)
    json_pictures = json.loads(date_pictures)
    images = []
    for image in range(len(picture_today)):
        if json_pictures[image]['media_type'] == 'image':
            images.append(json_pictures[image]['url'])
    return images


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token_nasa", help="token nasa", required=True)
    args = parser.parse_args()
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    images_nasa = get_nasa_apod_picture(nasa_url, args)
    load_image.get_images("nasa_image", images_nasa, parser)


if __name__ == '__main__':
    main()
