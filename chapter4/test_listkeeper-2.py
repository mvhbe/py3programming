import unittest
import listkeeper


class TestListkeeper(unittest.TestCase):

    def test_get_files_returns_a_list(self):
        """get_files returns a list"""
        files = listkeeper.get_files()
        self.assertTrue(type(files) is list)

    def test_get_files_returns_an_empty_list_when_no_files_present(self):
        """get_files returns an empty list when no files present"""
        files = listkeeper.get_files()
        self.assertEqual(len(files), 0, "number of files in not zero !")

if __name__ == '__main__':
    unittest.main(verbosity=2)
