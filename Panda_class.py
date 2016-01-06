import re


class Panda:

    def __init__(self, name, email, gender):
        self._name = name
        self._email = email
        if not self._is_mail_valid():
            raise Exception('Invalid mail !')
        self._gender = gender

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_gender(self):
        return self._gender

    def isMale(self):
        return self._gender == 'male'

    def isFemale(self):
        return not self.isMale()

    def _is_mail_valid(self):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.get_email()):
            return True
        return False

    def __str__(self):
        return 'Name>{}, Mail>{}, Gender>{}'.format(
                self.get_name(), self.get_email(), self.get_gender())

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_email() == other.get_email() and self.get_gender() == other.get_gender()

    def __hash__(self):
        return hash(str(self))


