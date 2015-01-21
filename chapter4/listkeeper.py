"""
Programming in Python 2 - Chapter 4 - Excercise

Interactive program that maintains a list of strings in files
"""
import os


def filter_lst_files(files):
    """
    return a list of files (*.lst)
    """
    return [lst_file for lst_file in files if lst_file.endswith(".lst")]


def ask_filename():
    """
    ask the user to provide a filename
    """
    return input("Choose filename : ")


def add_file_extension(filename):
    if not filename.endswith(".lst"):
        filename += ".lst"
    return filename


def create_file_list():
    files = filter_lst_files(os.listdir())
    if len(files) == 0:
        files = list(add_file_extension(ask_filename()))
    return files


def number_items(items=None):
    items = [] if items is None else items
    return (
        [str(number + 1) + ": " + item for number, item in enumerate(items)]
    )
