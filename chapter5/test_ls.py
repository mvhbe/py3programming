import os.path
import unittest
import ls


SIZE = 1365


def os_path_getsize(filename):
    return SIZE


def os_walk(directory):
    return None


class TestLs(unittest.TestCase):

    def setUp(self):
        self.ls = ls.Ls(path_walker=os_walk, size_reader=os_path_getsize)

    def tearDown(self):
        pass

    def test_optie_hidden_met_default_waarde_false_aanwezig(self):
        """Optie 'hidden' met default waarde 'False'"""
        self.assertFalse(self.ls.args.hidden, "Optie 'hidden' niet aanwezig !")

    def test_optie_modified_met_default_waarde_false_aanwezig(self):
        """Optie 'modified' met default waarde 'False'"""
        self.assertFalse(self.ls.args.modified, "Optie 'modified' niet aanwezig !")

    def test_optie_order_met_default_waarde_name_aanwezig(self):
        """Optie 'order' met default waarde 'name'"""
        self.assertEqual(self.ls.args.order, "name", "Optie 'order' niet aanwezig !")

    def test_optie_recursive_met_default_waarde_false_aanwezig(self):
        """Optie 'recursive' met default waarde 'False'"""
        self.assertFalse(self.ls.args.recursive, "Optie 'recursive' niet aanwezig !")

    def test_optie_sizes_met_default_waarde_false_aanwezig(self):
        """Optie 'sizes' met default waarde 'False'"""
        self.assertFalse(self.ls.args.sizes, "Optie 'sizes' niet aanwezig !")

    def test_optie_dirs_met_default_waarde_dot_aanwezig(self):
        """Optie 'dirs' met default waarde '.'"""
        self.assertIn(".", self.ls.args.dirs, "Optie 'dirs' niet aanwezig !")

    def test_verwijdert_verborgen_bestanden(self):
        """Functie 'remove_hidden' verwijdert verborgen bestanden/directories"""
        expected_dirnames = []
        dirnames = [".hidden_directory"]
        actual_dirnames = self.ls._remove_hidden(dirnames)
        self.assertEqual(expected_dirnames, actual_dirnames, "Verborgen bestanden niet verwijderd !")

    def test_verwijdert_geen_zichtbare_bestanden(self):
        """Functie 'remove_hidden' verwijdert geen zichtbare bestanden/directories"""
        expected_dirnames = ["zichtbaar"]
        dirnames = [".hidden_directory", "zichtbaar"]
        actual_dirnames = self.ls._remove_hidden(dirnames)
        self.assertEqual(expected_dirnames, actual_dirnames, "Verborgen bestanden niet verwijderd !")

    def test_grootte_bestand_wordt_opgehaald(self):
        """Functie _get_file_size geeft bestandsgrootte terug"""
        file_name = "./ls.py"
        expected_size = SIZE
        actual_size = self.ls._get_file_size(file_name)
        self.assertEqual(expected_size, actual_size, "Bestandsgrootte niet correct !")

    # def test_show_info_toont_size_bij_sizes_true(self):
    #     # os.path.getsize = get_size
    #     filename = "./ls.py"
    #     # self.ls.args = self.parser.parse_self.ls.args()
    #     self.ls.args.size = True
    #     output = self.ls.show_info(filename, self.ls.args)
    #     self.assertIn(str(SIZE), output, "Size wordt niet getoond !")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
