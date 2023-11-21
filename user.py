from enum import Enum
from typing import List


class Role(Enum):
    admin = "admin"
    user = "user"
class BaseUser():
    def __init__(self,name: [str], password: str, role: Role, email: str, phone: str,ind=None):
        self._name = name
        self._pass = password
        self._role = role
        self._email = email
        self._phone = phone
        self._index=ind
    def __str__(self):
        return f"{self.index},{self.name}, {self.password}, {self.role}, {self.email}, {self.phone}"

    # getters
    @property
    def name(self):
        return self._name
    @property
    def password(self):
        return self._pass
    @property
    def role(self):
        return self._role
    @property
    def email(self):
        return self._email
    @property
    def phone(self):
        return self._phone
    @property
    def index(self):
        return self._index
    @index.setter
    def index(self,ind):
        self._index=ind
class AdminUser(BaseUser):
    def __init__(self, name: [str], password: str, email: str, phone: str):
        super().__init__(name, password, Role.admin, email, phone)
class User(BaseUser):
    def __init__(self, name: [str], password: str, email: str, phone: str):
        super().__init__(name, password, Role.user, email, phone)