import unittest
from Panda_class import Panda
from PandaSocialNetwork import PandaSocialNetwork


class TestPandaClass(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.bg", "male")

    def test_get_name(self):
        self.assertEqual("Ivo", self.ivo.get_name())

    def test_get_email(self):
        self.assertEqual(self.ivo.get_email(), "ivo@pandamail.bg")

    def test_get_gender(self):
        self.assertEqual("male", self.ivo.get_gender())

    def test_isMale(self):
        maria = Panda("maria", "maria@pandamail.bg", "female")
        self.assertTrue(self.ivo.isMale())
        self.assertFalse(maria.isMale())

    def test_isFemale(self):
        maria = Panda("maria", "maria@pandamail.bg", "female")
        self.assertTrue(maria.isFemale())
        self.assertFalse(self.ivo.isFemale())

if __name__ == "__main__":
    unittest.main()
