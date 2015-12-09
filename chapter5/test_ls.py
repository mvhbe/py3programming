import unittest
import ls
from ls import DATE_FORMAT
from ls import FILE_SIZE_FORMAT


SIZE = 1365
FORMATTED_SIZE = FILE_SIZE_FORMAT.format(SIZE).replace(",", ".")
TIME = 1449229346.5816598
DATE_MODIFIED = "2015-12-04 11:42:26"


def getsize(filename):
    return SIZE


def getmtime(filename):
    return TIME


def walk(directory):
    return None


def strftime(DATE_FORMAT, time_stamp):
    return DATE_MODIFIED


class TestLs(unittest.TestCase):

    def setUp(self):
        self.ls = ls.Ls(walk=walk, getsize=getsize, getmtime=getmtime, strftime=strftime)

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
        """Functie '_remove_hidden' verwijdert verborgen bestanden/directories"""
        expected_dirnames = []
        dirnames = [".hidden_directory"]
        actual_dirnames = self.ls._remove_hidden(dirnames)
        self.assertEqual(expected_dirnames, actual_dirnames, "Verborgen bestanden niet verwijderd !")

    def test_verwijdert_geen_zichtbare_bestanden(self):
        """Functie '_remove_hidden' verwijdert geen zichtbare bestanden/directories"""
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


    def test_datum_laatste_wijziging_bestand_wordt_opgehaald(self):
        """Functie _get_date_modified geeft datum laatste wijziging terug"""
        file_name = "./ls.py"
        expected_date_modified = TIME
        actual_date_modified = self.ls._get_date_modified(file_name)
        self.assertEqual(expected_date_modified, actual_date_modified, "Datum laatste wijziging niet correct !")

    def test_format_date_modified_werk_correct(self):
        """Functie _format_date_modified werk correct"""
        expected_date = DATE_MODIFIED
        actual_date = self.ls._format_date_modified(TIME)
        self.assertEqual(expected_date, actual_date, "Datum formaat niet correct !")

    def test_format_file_size__werk_correct(self):
        """Functie _format_file_size werk correct"""
        expected_size = FORMATTED_SIZE
        actual_size = self.ls._format_file_size(SIZE)
        self.assertEqual(expected_size, actual_size, "Formaat bestandsgrootte niet correct !")


if __name__ == "__main__":
    unittest.main(verbosity=2)
