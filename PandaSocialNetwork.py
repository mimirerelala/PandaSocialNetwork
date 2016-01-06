class PandaSocialNetwork:
    def __init__(self):
        self.__pandas = {}

    def add_panda(self, panda):
        self.__pandas[panda] = []

    def has_panda(self, panda):
        if panda in self.__pandas:
            return True
        return False

    def make_friends(self, panda1, panda2):
        self.__pandas[panda1].append(panda2)
        self.__pandas[panda2].append(panda1)
        return

    def are_friends(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if panda2 in self.__pandas[panda1] and panda1 in self.__pandas[panda2]:
                return True
        return False

    def friends_of(self, panda):
        return self.__pandas[panda]

    def connection_level(self, panda1, panda2):

        return -1

    def are_connected(self, panda1, panda2):

        return False

    def how_many_gender_in_network(self, level, panda, gender):

        return 0
