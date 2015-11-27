import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H", "--hidden",
        action="store_true",
        help="show hidden files [default: off]",
        default=False
    )
    parser.add_argument(
        "-m", "--modified",
        action="store_true",
        help="show hidden last modified date/time [default: off]",
        default=False
    )
    parser.add_argument(
        "-o", "--order",
        help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]",
        default="name",
        choices=['name', 'n', 'modified', 'm', 'size', 's']
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="recurse into subdirectories [default: off]",
        default=False
    )
    parser.add_argument(
        "-s", "--sizes",
        action="store_true",
        help="show sizes [default: off]",
        default=False
    )
    parser.add_argument(
        "dirs",
        nargs="*",
        help="The dirs are optional. If not given, '.' is used.",
        default=list(".")
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("args = ", args)


if __name__ == "__main__":
    main()
