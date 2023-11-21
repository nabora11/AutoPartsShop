from db import *
import pandas as pd

class CustomOpsManager:
    def __init__(self,user_db_:UserDatabase,parts_db_:PartDataBase,basket:BasketDatabase):
        self.user_db=user_db_
        self.parts_db=parts_db_
        self.basket=basket

    def show_parts(self):
        return self.parts_db.db

    def search_part_by_name(self, name_: str) -> List[Part]:
        return self.parts_db.search_by_name(name_)

    def search_part_by_code(self, code_: int) -> Part:
        return self.parts_db.search_by_code(code_)

    def get_basket(self):
        return BasketDatabase.get_basket()

    def get_basket_price(self):
        return  BasketDatabase.get_basket_price()

    def add_to_basket(self,part_: Part):
        BasketDatabase.add_new_entry(part_)
class AdminOpsManager(CustomOpsManager):
    def __init__(self,user_db_:UserDatabase,parts_db_:PartDataBase,basket:BasketDatabase):
        super().__init__(user_db_,parts_db_,basket)

    def add_part(self, part: Part, db_: UserDatabase):
        self.parts_db.add(part,db_)

    def remove_part_by_name(self, name: str,user_db:UserDatabase):
        self.parts_db.remove_by_name(name,user_db)

    def remove_part_by_code(self, code_: int, user_db: UserDatabase):
        return self.parts_db.remove_by_code(code_, user_db)

    def remove_part_by_index(self, indx: int, user_db: UserDatabase):
        return self.parts_db.remove_by_index(indx,user_db)

    def show_users(self):
        return  self.user_db.db

    def add_user(self, user: BaseUser):
        self.user_db.add(user)

    def remove_user_by_name(self, name: str):
        self.user_db.remove_by_name(name)

    def remove_user_by_mail(self, mail: str):
        self.user_db.remove_by_mail(mail)

    def remove_user_by_index(self, indx: int):
        self.user_db.remove_by_index(indx)

    def search_user_by_name(self, name: str) -> List[BaseUser]:
        return self.user_db.search_by_name(name)

    def search_user_by_mail(self, mail: str) -> BaseUser:
        return self.user_db.search_by_mail(mail)