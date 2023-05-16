import requests
import argparse
import load_image


def get_nasa_apod_picture(args):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'start_date': "2023-03-15",
        'end_date': "2023-04-15",
        'api_key': args.token_nasa
    }
    response = requests.get(nasa_url, params=params)
    picture_today = response.json()
    images = []
    for image in range(len(picture_today)):
        if picture_today[image]['media_type'] == 'image':
            images.append(picture_today[image]['url'])
    return images


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token_nasa", help="token nasa", required=True)
    args = parser.parse_args()
    images_nasa = get_nasa_apod_picture(nasa_url, args)
    load_image.get_images("nasa_image", images_nasa, parser)


if __name__ == '__main__':
    main()
