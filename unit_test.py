import unittest
from Panda_class import Panda
from PandaSocialNetwork import PandaSocialNetwork


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.ivo = Panda("Ivo", "ivo@pandamail.bg", "male")
        self.network = PandaSocialNetwork()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.network.has_panda(self.ivo))

    def test_has_panda_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.bg", "male")
        self.assertFalse(self.network.has_panda(rado))

    def test_make_and_are_friends(self):
        rado = Panda("Rado", "rado@pandamail.bg", "male")
        self.network.make_friends(self.ivo, rado)
        self.assertTrue(self.network.are_friends(self.ivo, rado))

    def test_connection_level(self):
        m=1
        
if __name__ == "__main__":
    unittest.main()