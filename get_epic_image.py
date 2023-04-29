import requests
import argparse
import load_image


def get_epic_picture(epic_url, args):
    if args.token_epic:
        params = {
            'apy_key': args.token_epic
        }
        response = requests.get(epic_url, params=params)
    else:
        response = requests.get(epic_url)
    response_json = response.json()
    epic_list = []
    for image in range(10):
        if response_json[image]['image'] and response_json[image]['date']:
            image_name = response_json[image]['image']
            image_date = response_json[image]['date']
            image_date_split = image_date[0:10].replace('-', '/')
            epic_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date_split}/png/{image_name}.png?api_key=DEMO_KEY"
            epic_list.append(epic_image_url)
    return epic_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token_epic", help="token epic")
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
    args = parser.parse_args()
    image_epic_list = get_epic_picture(epic_url, args)
    print(image_epic_list)
    load_image.get_images("epic_image", image_epic_list)


if __name__ == '__main__':
    main()