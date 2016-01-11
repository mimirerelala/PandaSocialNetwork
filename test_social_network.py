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
        rado = Panda("Rado", "rado@pandamail.bg", "male")
        self.network.make_friends(self.ivo, rado)
        self.assertEqual(self.network.connection_level(self.ivo, rado), 1)

    def test_are_connected(self):
        rado = Panda("Rado", "rado@pandamail.bg", "male")
        self.network.make_friends(self.ivo, rado)
        self.assertTrue(self.network.are_connected(self.ivo, rado))
        mimi = Panda("Mimi", "mimi@pandamail.bg", "female")
        self.assertFalse(self.network.are_connected(self.ivo, mimi))
        self.network.make_friends(rado, mimi)
        self.assertTrue(self.network.are_connected(mimi, rado))

    def test_genders_in_level(self):

        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "female")
        maria = Panda("maria", "maria@pandamail.com", "female")
        ivo = Panda("Ivo", "ivo@pandamail.bg", "male")
        niki = Panda("Niki", "niki@mail.com", 'male')
 
        self.network.add_panda(rado)
        self.network.add_panda(pavli)
        self.network.add_panda(maria)
        self.network.add_panda(ivo)
        self.network.add_panda(niki)
 
        self.network.make_friends(ivo, rado)
        self.network.make_friends(rado, pavli)
        self.network.make_friends(pavli, maria)
        self.network.make_friends(rado, niki)

        self.assertEqual(self.network.how_many_gender_in_network(3, maria, 'male'),3)

if __name__ == "__main__":
    unittest.main()
