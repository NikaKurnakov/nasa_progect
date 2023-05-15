import requests
import os


def get_images(filename, images, parser):
    os.makedirs("images", exist_ok=True)
    args = parser.parse_args()
    args_parser = vars(parser.parse_args())
    for image_number, image in enumerate(images):
        filename1 = os.path.join("images", f"{filename}_{image_number}.png")
        if "token_epic" in args_parser:
            params = {
                'api_key': args.token_epic,
            }
            response = requests.get(image, params=params)
        elif "token_nasa" in args_parser:
            params = {
                'api_key': args.token_nasa
            }
            response = requests.get(image, params=params)
        else:
            response = requests.get(image)
        if response.ok:
            with open(filename1, 'wb') as file:
                file.write(response.content)
