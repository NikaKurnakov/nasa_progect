import requests
import json
import argparse
import load_image



def nasa_apod(nasa_url, args):
    if args.token_nasa:
        params = {
            'start_date': "2023-03-15",
            'end_date': "2023-04-15",
            'api_key': args.token_nasa
        }
        response = requests.get(nasa_url, params=params)
    else:
        response = requests.get(nasa_url)
    picture_today = response.json()
    date_pictures = json.dumps(response.json())
    json_pictures = json.loads(date_pictures)
    image_list = []
    for image in range(len(picture_today)):
        if json_pictures[image]['media_type'] == 'image':
            image_list.append(json_pictures[image]['url'])
    return image_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token_nasa", help="token nasa")
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    args = parser.parse_args()
    image_nasa_list = nasa_apod(nasa_url, args)
    print(image_nasa_list)
    load_image.get_images("nasa_image", image_nasa_list)


if __name__ == '__main__':
    main()