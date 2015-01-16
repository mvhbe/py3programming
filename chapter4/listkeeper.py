"""
Programming in Python 2 - Chapter 4 - Excercise

Interactive program that maintains a list of strings in files
"""
import os


def get_lst_files():
    """
    return a list of files (*.lst)
    """
    return [lst_file for lst_file in os.listdir(".") if lst_file.endswith(".lst")]


