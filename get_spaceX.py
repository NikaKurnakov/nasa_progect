import requests
import json
import argparse
import load_image


def get_one_launch(url, args):
    if args.id:
        params = {
            'id': args.id
        }
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)
    data = json.dumps(response.json())
    json_file = json.loads(data)
    for image in range(len(json_file)):
        if json_file[-image]['links']['flickr']['original']:
            return json_file[-image]['links']['flickr']['original']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id интересующей картинки")
    args = parser.parse_args()
    url = "https://api.spacexdata.com/v5/launches/"
    image_spaceX_list = get_one_launch(url, args)
    print(image_spaceX_list)
    load_image.get_images('spaceX_image', image_spaceX_list)


if __name__ == '__main__':
    main()