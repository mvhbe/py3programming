import argparse
import os
import os.path


class Ls(object):

    def __init__(self, path_walker=os.walk, size_reader=os.path.getsize):
        self.path_walker = path_walker
        self.size_reader = size_reader
        self.parser = self._create_parser()
        self.args = self.parser.parse_args()

    def _create_parser(self):
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

    def _get_file_size(self, file_name):
        return self.size_reader(file_name)

    def _remove_hidden(self, names):
        return [name for name in names if not name.startswith(".")]

    def show_info(self, filename, args):
        return ""
    
    
def main():
    ls = Ls()
    print("args = ", ls.args)


if __name__ == "__main__":
    main()
