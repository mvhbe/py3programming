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
    def test_get_lst_files_returns_a_list(self):
        """
        get_lst_files returns a list
        """
        files = listkeeper.get_lst_files()
        self.assertTrue(type(files) is list)

    def test_get_lst_files_returns_an_empty_list_when_no_lst_files_present(self):
        """
        get_lst_files returns an empty list when no files (*.lst) present
        """
        files = listkeeper.get_lst_files()
        nr_of_files = len(files)
        self.assertEqual(nr_of_files, 0, "number of files ({}) is not zero !".format(nr_of_files))

if __name__ == '__main__':
    unittest.main(verbosity=2)
