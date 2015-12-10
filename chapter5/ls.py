import argparse
import os
import os.path
import time


DATE_FORMAT = "%Y-%m-%d %H:%M:%S "
FILE_SIZE_FORMAT = "{:10,d}"


class Ls(object):

    def __init__(self, walk=os.walk, getsize=os.path.getsize, getmtime=os.path.getmtime, strftime=time.strftime):
        self.walk = walk
        self.getsize = getsize
        self.getmtime= getmtime
        self.strftime = strftime
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
            help="show last modified date/time [default: off]",
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
        return self.getsize(file_name)

    def _get_date_modified(self, file_name):
        return self.getmtime(file_name)

    def _remove_hidden(self, names):
        return [name for name in names if not name.startswith(".")]

    def _format_date_modified(self, time_stamp):
        return self.strftime(DATE_FORMAT, time.gmtime(time_stamp))

    def _format_file_size(self, file_size):
        return FILE_SIZE_FORMAT.format(file_size).replace(",", ".")


def main():
    ls = Ls()
    print("args = ", ls.args)


if __name__ == "__main__":
    main()
