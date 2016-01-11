from collections import deque
from Panda_class import Panda


class PandaSocialNetwork:
    def __init__(self):
        self.__pandas = {}

    def add_panda(self, panda):
        if not self.has_panda(panda):
            self.__pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.__pandas

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if not self.are_friends(panda1, panda2):
            self.__pandas[panda1].append(panda2)
            self.__pandas[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if panda2 in self.__pandas[panda1] and panda1 in self.__pandas[panda2]:
                return True
        return False

    def friends_of(self, panda):
        return self.__pandas[panda]

    def _bfs_with_level(self, start_node, end_node):
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append((0, start_node))

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if node == end_node:
                return level

            for neighbour in self.__pandas[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))

        return -1

    def _bfs_gender_counter(self, levels, start_node, gender):
        visited = set()
        queue = deque()

        visited.add(start_node)
        queue.append((0, start_node))

        gender_counter = 0

        while len(queue) != 0:
            node_with_level = queue.popleft()
            node = node_with_level[1]
            level = node_with_level[0]

            if level == levels:
                for panda in visited:
                    if panda.get_gender() == gender:
                        gender_counter += 1
                if start_node.get_gender() == gender:

                    gender_counter -= 1
                return gender_counter

            for neighbour in self.__pandas[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((level + 1, neighbour))

        return -1

    def connection_level(self, panda1, panda2):

        if panda1 not in self.__pandas or panda2 not in self.__pandas:
            return False

        return self._bfs_with_level(panda1, panda2)

    def are_connected(self, panda1, panda2):

        return self._bfs_with_level(panda1, panda2) > 0

    def how_many_gender_in_network(self, level, panda, gender):

        return self._bfs_gender_counter(level, panda, gender)
