from typing import Tuple
from support_functions import *
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def welcome_screen_view():
    print("""
    Welcome to online auto-parts shopping: 
    1. Login
    2. Register
    3. Exit
    
    Enter number (1,2 or 3): """,end='')

def login_screen_view()->Tuple[str,str]:
    clear_screen()
    print("\nPlease enter your email and password:")
    mail=input('Email: ')
    code=input('Password: ')
    keyboard.read_event()
    return (mail,code)
def register_screen_view()->User:
    print("""\nPlease enter your email and password:
            password should be from 5 to 9 symbols""")
    mail = input('Email: ')
    code1=''
    while len(code1)<5 or len(code1)>9:
        code1 = input('Password: ')
    code2=''
    while code1!=code2:
        code2 = input('Password again: ')
        if code1!=code2: print('password not match, enter again')
    print('Please provide fallowing user information:')
    name=list(input("Two names:").split(sep=' '))
    phone=input('Phone:')
    return User(name,code1,mail,phone)
def custom_screenview():
    print("""
        \nPlease choose number from the menu: 
        1. Show all parts
        2. Search part by part's name
        3. Search part by part's code
        4. Show basket
        5. Add to basket
        6. Proceed to payment
        7. Exit
        
        Enter number 1,2,3,4,5,6 or 7:  """,end='')
def admin_main_screenview():
    print("""
        \nPlease choose number from the menu: 
        1. User database management
        2. Parts database management
        3. Exit
        
        Enter number 1,2,3:  """,end='')
def admin_userops_screenview():
    print("""
        \nPlease choose number from the menu: 
        1. Show all users
        2. Search user by name
        3. Search user by mail
        4. Remove user by name
        5. Remove user by index
        6. Remove user by mail
        7. Add new user
        8. Return to main menu
        
        Enter number 1,2,3,4,5,6,7 or 8:  """,end='')
def admin_partops_screenview():
    print("""
            \nPlease choose number from the menu: 
            1. Show all parts
            2. Search part by name
            3. Search part by code
            4. Remove part by name
            5. Remove part by code
            6. Add new part
            7. Return to main menu
            
            Enter number 1,2,3,4,5,6 or 7:  """, end='')
def search_part_by_name_view()->str:
    print("\nInput part name to search: ")
    while True:
        ret=input()
        if ret.isalpha(): break
    return ret
def search_part_by_code_view()->str:
    print("\nInput part code to search: ")
    while True:
        ret=input()
        if ret.isdigit(): break
    return ret
def add_to_basket_view()->str:
    print("\nInput the code of the part to add: ")
    while True:
        ret=input()
        if ret.isdigit(): break
    return ret
def search_user_by_name_view()->str:
    print("Input  name of user: ")
    while True:
        ret=input()
        if ret.isalpha() and len(ret)>3: break
    return ret
def search_user_by_mail_view()->str:
    print("\nInput user mail to search: ")
    while True:
        ret=input()
        if len(ret)>3: break
    return ret
def search_user_by_index_view()->int:
    print("\nInput user index to remove: ")
    while True:
        try:
            ret = int(input())
            break
        except ValueError:
            print('Please insert int:\n')
    return ret
def add_new_user_view()->BaseUser:
    user=register_screen_view()
    print("""Please choose the role of the user:
    1. Admin
    2. Customer""")
    # keyboard.read_event()
    key=key_get(2)
    if key=='1': role_=Role.admin
    elif key=='2': role_=Role.user
    else: raise KeyError
    return BaseUser(user.name,user.password,role_,user.email,user.phone)
def add_new_part_view()->Part:
    print("\n please provide fallowing information:")
    code_=int(input("1. code of the part (4 digits): "))
    name_=input("2. part name: ")
    print("""3. part category: 
    1. TRUCK,
    2. WHEELS,
    3. ENGINE,
    4. ACCESSORIES""")
    # keyboard.read_event()
    key = key_get(4)
    if key=='1':category_=PartsCategory.TRUCK
    elif key=='2':category_=PartsCategory.WHEELS
    elif key=='3':category_=PartsCategory.ENGINE
    elif key=='4':category_=PartsCategory.ACCESSORIES
    else: raise KeyError
    buy_=input('\n4. buy price (float): ')
    sell_=input('\n5. sell price (float): ')
    cars_=list(input('\n6. models of cars to wich is applicable (sep=\',\'): ').split(','))
    return Part(code_,name_,category_,buy_,sell_,cars_)