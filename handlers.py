from login_register import *
import  sys
from account_ops_management import *
from support_functions import *
from views import *
from db import *

def welcome_screen_handler(parts_db: PartDataBase, user_db: UserDatabase):
    welcome_screen_view()
    a=key_get(3)
    if a=='1':
        login_screen_handler(parts_db, user_db)
    if a=='2':
        register_screen_handler(parts_db, user_db)
    if a=='3':
        exit_handler(parts_db, user_db)
def custom_ops_handler(parts_db: PartDataBase, user_db: UserDatabase):
    manager=CustomOpsManager(user_db,parts_db,BasketDatabase)
    try:
        while True:
            custom_screenview()
            a=key_get(7)
            if a=='1':
                print()
                print(manager.show_parts())
                wait()
                continue
            elif a=='2':
                part=search_part_by_name_view()
                found=manager.search_part_by_name(part)
                print(customer_diplay_parts_as_df(found))
                wait()
                continue
            elif a=='3':
                part = int(search_part_by_code_view())
                found = manager.search_part_by_code(part)
                found=[found,]
                print(customer_diplay_parts_as_df(found))
                wait()
                continue
            elif a=='4':
                print()
                print(manager.get_basket())
                wait()
                continue
            elif a=='5':
                part=int(add_to_basket_view())
                found_ = manager.search_part_by_code(part)
                if not found_:
                    print("Part not found in database")
                manager.add_to_basket(found_)
                print(manager.get_basket())
                wait()
                continue
            elif a=='6':
                print()
                print()
                print(manager.get_basket())
                print()
                print(manager.get_basket_price())
                wait()
                continue
            elif a=='7':
                exit_handler(parts_db, user_db)
                break
            else:
                print(a)
    except Exception as e:
        e_type, e_object, e_traceback = sys.exc_info()
        print("Error",e)
        print("Type: ",e_type)
        print("Line : ",e_traceback.tb_lineno)
def admin_mainops_handler(parts_db: PartDataBase, user_db: UserDatabase):
    manager=AdminOpsManager(user_db,parts_db,BasketDatabase)
    try:
        while True:
            admin_main_screenview()
            a=key_get(3)
            if a=='1':
                print()
                admin_userops_handler(manager)
                continue
            elif a=='2':
                print()
                admin_partops_handler(manager)
                continue
            elif a=='3':
                exit_handler(parts_db, user_db)
                break
    except Exception as e:
        e_type, e_object, e_traceback = sys.exc_info()
        print("Error",e)
        print("Type: ",e_type)
        print("Line : ",e_traceback.tb_lineno)
def admin_userops_handler(manager_:AdminOpsManager):
    while True:
        admin_userops_screenview()
        a = key_get(8)
        if a == '1':
            print()
            print(manager_.show_users())
            wait()
            continue
        elif a == '2':
            print()
            for el in manager_.search_user_by_name(search_user_by_name_view()):
                print(el)
            wait()
            continue
        elif a == '3':
            print()
            a=search_user_by_mail_view()
            print(manager_.search_user_by_mail(a))
            wait()
            continue
        elif a == '4':
            print('\nRemoving user by Name!')
            a = search_user_by_name_view()
            manager_.remove_user_by_name(a)
            wait()
            continue
        elif a == '5':
            print('\nRemoving user by Index!')
            a = search_user_by_index_view()
            manager_.remove_user_by_index(a)
            wait()
            continue
        elif a == '6':
            print('\nRemoving user by mail!')
            a = search_user_by_mail_view()
            manager_.remove_user_by_mail(a)
            wait()
            continue
        elif a == '7':
            user=add_new_user_view()
            manager_.add_user(user)
            print('/n user ',user.email,' successfully added')
            wait()
            continue
        elif a == '8':
            return
def admin_partops_handler(manager_:AdminOpsManager):
    while True:
        admin_partops_screenview()
        a = key_get(8)
        if a == '1':
            print()
            print(manager_.show_parts())
            wait()
            continue
        elif a == '2':
            print()
            b=search_part_by_name_view()
            for el in manager_.search_part_by_name(b):
                print(el.admin_info())
            wait()
            continue
        elif a == '3':
            print()
            a = int(search_part_by_code_view())
            print(manager_.search_part_by_code(a))
            wait()
            continue
        elif a == '4':
            print('\nRemoving part by name!')
            a = search_part_by_name_view()
            manager_.remove_part_by_name(a,manager_.user_db)
            wait()
            continue
        elif a == '5':
            print('\nRemoving part by code!')
            a = int(search_part_by_code_view())
            manager_.remove_part_by_code(a,manager_.user_db)
            wait()
            continue
        elif a == '6':
            part_ = add_new_part_view()
            manager_.add_part(part_,manager_.user_db)
            1
            wait()
            continue
        elif a == '7':
            return
def login_screen_handler(parts_db: PartDataBase, user_db: UserDatabase):
    # mail_,pass_=login_screen_view()
    mail_,pass_="koko@abv.bg","kiki0944"
    # # mail_,pass_="babayaga@abv.bg","baba88"

    if login(mail_,pass_,user_db):
        print(f'\nSuccessfully loged in {mail_}')
        custom_ops_handler(parts_db,user_db) if user_db.get_current_user().role==Role.user else admin_mainops_handler(parts_db,user_db)
    else:
        print('Login failed')
        welcome_screen_handler(parts_db, user_db)
def register_screen_handler(parts_db: PartDataBase, user_db: UserDatabase):
    user_=register_screen_view()
    if register(user_,user_db):
        print("Registration successfully completed")
        welcome_screen_handler(parts_db,user_db)
    else:
        print('Registration failed')
        welcome_screen_handler(parts_db, user_db)
def exit_handler(parts_db: PartDataBase, user_db: UserDatabase):
    parts_db.sync_shutdown()
    user_db.sync_shutdown()
