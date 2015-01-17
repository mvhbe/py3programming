"""
Programming in Python 2 - Chapter 4 - Excercise

Interactive program that maintains a list of strings in files
"""
import unittest
import listkeeper


class TestListkeeper(unittest.TestCase):
    """
    Tests for the interactive program that maintains a list of strings in files
    """
    def test_filter_lst_files_returns_a_list(self):
        """
        filter_lst_files returns a list
        """
        files = listkeeper.filter_lst_files([])
        self.assertTrue(type(files) is list)

    def test_filter_lst_files_returns_an_empty_list_when_no_lst_files_present(self):
        """
        filter_lst_files returns an empty list when no files (*.lst) present
        """
        files = ["file1.doc", "file2.xls", "file3.txt"]
        lst_files = listkeeper.filter_lst_files(files)
        nr_of_files = len(lst_files)
        self.assertEqual(nr_of_files, 0, "number of files ({}) is not zero !".format(nr_of_files))

    def test_filter_lst_files_returns_only_lst_files(self):
        """
        filter_lst_files only returns files ending with .lst
        """
        files = ["file1.doc", "file2.xls", "file3.txt", "file4.lst", "file5.lst"]
        lst_files = listkeeper.filter_lst_files(files)
        self.assertTrue(all(['.lst' in file_name for file_name in lst_files]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
