"""
short describtion of used objects and functions in this program:

views.py-> taking all inputs and send to handlers;

handlers.py-> manages user input from console (from view.py) and communicates with databases (db.py) through
user or admin operations managers (account_ops_management.py) depends on the role of the user (admin or user)

account_ops_management.py-> defines two objects : AdminOpsManager and CustomOpsManager with necessary allowed
actions and operations

user.py-> defines objects BaseUser, AdminUser and User

part.py-> defines class Part

support_functions.py-> defines usefull functions to support the process

connection to UserDatabase and PartDatabase storage files is controlled by using Pandas
"""


from db import PartDataBase,CsvPartDataBase,UserDatabase,BaseUser,AdminUser
from handlers import welcome_screen_handler
from pathlib import Path
import pandas as pd

if __name__=="__main__":
    pd.set_option("display.max_columns",None)
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_colwidth', 500)
    pd.set_option('display.colheader_justify', 'center')


    path_parts=Path("parts.csv")
    data_parts=CsvPartDataBase(path_parts)
    path_users=Path("users.pickle")
    data_users=UserDatabase(path_users)
    # print(data_users)
    welcome_screen_handler(data_parts,data_users)
