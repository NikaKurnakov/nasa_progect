import requests
import json
import argparse
import load_image


def get_one_launch(spaceX_url, parser, args):
    args_dict = vars(parser.parse_args())
    if "id" in args_dict:
        params = {
            'id': args.id
        }
        response = requests.get(spaceX_url, params=params)
    else:
        response = requests.get(spaceX_url)
    data_json = response.json()
    data = json.dumps(data_json)
    json_file = json.loads(data)
    for image in range(len(json_file)):
        image_path = json_file[-image]['links']['flickr']['original']
        if image_path:
            return image_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id интересующей картинки")
    args = parser.parse_args()
    spaceX_url = "https://api.spacexdata.com/v5/launches/"
    image_spaceX_list = get_one_launch(spaceX_url, parser, args)
    load_image.get_images('spaceX_image', image_spaceX_list, parser)


if __name__ == '__main__':
    main()
