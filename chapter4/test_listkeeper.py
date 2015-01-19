#!/usr/bin/env python3
"""
Programming in Python 2 - Chapter 4 - Excercise

Interactive program that maintains a list of strings in files
"""
from unittest.mock import patch
import unittest
import listkeeper


def input(prompt):
    """mock builtin function input()"""
    return "filename"

def empty_dir(files):
    """mock an empty directory"""
    return []


class TestListkeeper(unittest.TestCase):
    """
    Tests for the interactive program that maintains a list of strings in files
    """
    def test_filter_lst_files_returns_a_list(self):
        """filter_lst_files returns a list"""
        files = listkeeper.filter_lst_files([])
        self.assertTrue(type(files) is list)

    def test_filter_lst_files_returns_an_empty_list_when_no_lst_files_present(self):
        """filter_lst_files returns an empty list when no files (*.lst) present"""
        files = ["file1.doc", "file2.xls", "file3.txt"]
        lst_files = listkeeper.filter_lst_files(files)
        nr_of_files = len(lst_files)
        self.assertEqual(nr_of_files, 0, "number of files ({}) is not zero !".format(nr_of_files))

    def test_filter_lst_files_returns_only_lst_files(self):
        """filter_lst_files only returns files ending with .lst"""
        files = ["file1.doc", "file2.xls", "file3.txt", "file4.lst", "file5.lst"]
        lst_files = listkeeper.filter_lst_files(files)
        self.assertTrue(all(['.lst' in file_name for file_name in lst_files]))

    @patch('builtins.input', side_effect=input)
    def test_ask_file_name_returns_a_string(self, input_function):
        """ask_filename returns a string for the filename"""
        file_name = listkeeper.ask_filename()
        self.assertTrue(type(file_name) is str)

    def test_add_file_extension_adds_extension_if_no_extension(self):
        """add_file_extension adds '.lst' if filename doesn't end with '.lst'"""
        expected_filename = "filename.lst"
        filename = listkeeper.add_file_extension("filename")
        self.assertEqual(expected_filename, filename)

    def test_add_file_extension_adds_nothing_if_lst_extension_is_present(self):
        """add_file_extension adds nothing if filename ends with '.lst'"""
        expected_filename = "filename.lst"
        filename = listkeeper.add_file_extension("filename.lst")
        self.assertEqual(expected_filename, filename)

    @patch('builtins.input', side_effect=input)
    def test_create_file_list_returns_a_list(self, mock_function):
        """create_file_list returns a list"""
        files = listkeeper.create_file_list()
        self.assertTrue(type(files), list)

    @patch('builtins.input', side_effect=input)
    @patch("listkeeper.filter_lst_files", side_effect=empty_dir)
    def test_create_file_list_returns_the_entered_filename_when_no_lst_files_present(self, function1, function2):
        """create_file_list returns a an empty list when no .lst files present"""
        files = listkeeper.create_file_list()
        expected_files = list("filename.lst")
        self.assertEqual(expected_files, files)

if __name__ == '__main__':
    unittest.main(verbosity=2)
