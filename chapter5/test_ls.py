import unittest
import ls


class TestLs(unittest.TestCase):

    def setUp(self):
        self.parser = ls.create_parser()

    def tearDown(self):
        pass

    def test_optie_hidden_met_default_waarde_false_aanwezig(self):
        """Optie 'hidden' met default waarde 'False'"""
        args = self.parser.parse_args()
        self.assertFalse(args.hidden, "Optie 'hidden' niet aanwezig !")

    def test_optie_modified_met_default_waarde_false_aanwezig(self):
        """Optie 'modified' met default waarde 'False'"""
        args = self.parser.parse_args()
        self.assertFalse(args.modified, "Optie 'modified' niet aanwezig !")

    def test_optie_order_met_default_waarde_name_aanwezig(self):
        """Optie 'order' met default waarde 'name'"""
        args = self.parser.parse_args()
        self.assertEqual(args.order, "name", "Optie 'order' niet aanwezig !")

    def test_optie_recursive_met_default_waarde_false_aanwezig(self):
        """Optie 'recursive' met default waarde 'False'"""
        args = self.parser.parse_args()
        self.assertFalse(args.recursive, "Optie 'recursive' niet aanwezig !")

    def test_optie_sizes_met_default_waarde_false_aanwezig(self):
        """Optie 'sizes' met default waarde 'False'"""
        args = self.parser.parse_args()
        self.assertFalse(args.sizes, "Optie 'sizes' niet aanwezig !")

    def test_optie_dirs_met_default_waarde_dot_aanwezig(self):
        """Optie 'dirs' met default waarde '.'"""
        args = self.parser.parse_args()
        self.assertIn(".", args.dirs, "Optie 'dirs' niet aanwezig !")


if __name__ == "__main__":
    unittest.main(verbosity=2)
