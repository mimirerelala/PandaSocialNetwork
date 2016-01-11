from PandaSocialNetwork import *
from Panda_class import *


ivo = Panda("Ivo", "ivo@pandamail.com", "male")

ivo.get_name() == "Ivo" # True
ivo.get_email() == "ivo@pandamail.com"  # True
ivo.get_gender() == "male" # True
ivo.isMale() == True # True
ivo.isFemale() == False # True


network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

#network.make_friends(ivo, rado)
#network.make_friends(rado, tony)

network.connection_level(ivo, rado) == 1 # True
network.connection_level(ivo, tony) == 2 # True

network.how_many_gender_in_network(1, rado, "female") == 1 # True