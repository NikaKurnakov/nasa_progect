import requests
import argparse
import load_image


def get_one_launch(parser, args):
    spaceX_url = "https://api.spacexdata.com/v5/launches/"
    args_parser = vars(parser.parse_args())
    if "id" in args_parser:
        params = {
            'id': args.id
        }
        response = requests.get(spaceX_url, params=params)
    else:
        response = requests.get(spaceX_url)
    data_json = response.json()
    for image in range(len(data_json)):
        image_path = data_json[-image]['links']['flickr']['original']
        if image_path:
            return image_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id интересующей картинки")
    args = parser.parse_args()
    images_spaceX = get_one_launch(spaceX_url, parser, args)
    load_image.get_images('spaceX_image', images_spaceX, parser)


if __name__ == '__main__':
    main()
