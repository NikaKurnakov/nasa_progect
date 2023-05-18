import requests
import argparse
import load_image


def get_one_launch(params):
    spaceX_url = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(spaceX_url, params=params)
    data_json = response.json()
    for image in range(len(data_json)):
        image_path = data_json[-image]['links']['flickr']['original']
        if image_path:
            return image_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="id интересующей картинки")
    args = parser.parse_args()
    args_parser = vars(parser.parse_args())
    if "id" in args_parser:
        params = {
            'id': args.id
        }
    else:
        params = {}
    images_spaceX = get_one_launch(params)
    load_image.get_images('spaceX_image', images_spaceX, params)


if __name__ == '__main__':
    main()
