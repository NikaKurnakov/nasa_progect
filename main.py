import os


def get_expansion(expansion_url):
    split = os.path.split(expansion_url)[1]
    splitext = os.path.splitext(split)[1]
    print(splitext)

def main():
    expansion_url = input("введите ссылку:")
    get_expansion(expansion_url)


if __name__ == '__main__':
    main()