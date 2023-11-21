import keyboard
import pandas as pd
from typing import List, LiteralString,Tuple
from user import *
from part import *




def key_get(n:int)->str:
    while True:
        event = keyboard.read_event()
        if event.name=='enter':continue
        if event.event_type == keyboard.KEY_UP:
            key = event.name
            if int(key) in range(1,n+1):
                return key
def wait():
    print("\npress 'ENTER' to continue")
    keyboard.wait('enter')
    keyboard.read_key()
def customer_diplay_parts_as_df(parts_:List[Part])->pd.DataFrame:
    df = pd.DataFrame(
        {'Code': [el.code for el in parts_],
         'Name': [el.name for el in parts_],
         'Category': [el.category for el in parts_],
         'Price': [el.sell_price for el in parts_],
         'Cars': [el.list_of_cars for el in parts_]},
        columns=['Code', 'Name', 'Category', 'Price', 'Cars'])
    return df
def passed_permit_check(user: BaseUser or None) -> bool:
    if user == None: return False
    if user.role == Role.admin: return True
    return False
def user_from_df(df:pd.DataFrame,ind:int):
    return BaseUser(df['Name'],df['Password'],df['Role'],df['Email'],df['Phone'],ind)

#User defined exceptions
class PartAlreadyExistError(Exception):
    pass
class PartNotFoundError(Exception):
    pass
class DataFileError(Exception):
    pass
class IndexNotFoundError(Exception):
    pass
class FileNotExistError(Exception):
    pass
class UserAlreadyExistError(Exception):
    pass
class NotAuthorisedAccessError(Exception):
    pass
class UserNotFoundError(Exception):
    pass
class NotAutorisedError(Exception):
    pass