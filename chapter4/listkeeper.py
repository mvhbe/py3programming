"""
Programming in Python 2 - Chapter 4 - Excercise

Interactive program that maintains a list of strings in files
"""


def filter_lst_files(files):
    """
    return a list of files (*.lst)
    """
    return [lst_file for lst_file in files if lst_file.endswith(".lst")]


