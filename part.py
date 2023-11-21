from enum import Enum
from typing import List

class PartsCategory(Enum):
    TRUCK=1,
    WHEELS=2,
    ENGINE=3,
    ACCESSORIES=4

class Part:
    def __init__(self,code:int,name:str, cat:PartsCategory,buy_price:float, sell_price:float
                 ,list_cars:List):
        self._code=code
        self._name=name
        self._cat=cat
        self._buy_price=buy_price
        self._sell_price=sell_price
        self._list_cars=list_cars

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._cat

    @property
    def buy_price(self):
        return self._buy_price

    @property
    def sell_price(self):
        return self._sell_price

    @property
    def list_of_cars(self):
        return self._list_cars

    def __str__(self):
        return f"{self.code},{self.name},{self.category},{self.buy_price},{self.sell_price},{self.list_of_cars}"
    def customer_info(self):
        return ('{} {} {} {} {}'.format(self._code,self.name,self.category,self.sell_price,self.list_of_cars))
    def admin_info(self):
        return ('{} {} {} {} {} {}'.format(self._code,self.name,self.category,self.buy_price,self.sell_price,self.list_of_cars))

