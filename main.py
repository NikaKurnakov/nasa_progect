import os
import argparse


def get_expansion(args):
    if args.url:
        split = os.path.split(args.url)[1]
        splitext = os.path.splitext(split)[1]
        print(splitext)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="url split")
    args = parser.parse_args()
    get_expansion(args)
