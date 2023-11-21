from pathlib import Path
from support_functions import *


class UserDatabase:
    current_user = None

    @staticmethod
    def set_current_user(user: BaseUser or None):
        UserDatabase.current_user = user

    @staticmethod
    def get_current_user() -> BaseUser or None:
        return UserDatabase.current_user

    def __init__(self, path: Path):
        if path.exists():
            self._path = path
            self._db = pd.DataFrame
            self.sync_init()
        else:
            raise FileNotExistError
    def __str__(self):
        data_list=[BaseUser]
        i=1
        for ind, cur_user in self._db.iterrows():
            data_list.append(user_from_df(cur_user,i))
            i+=1
        data_str='\n'.join(str(x) for x in data_list)
        return str(data_str)
    def sync_init(self):
        self._db = pd.read_pickle(self._path)

    def sync_shutdown(self):
        self._db.reset_index(drop=True, inplace=True)
        self._db.to_pickle(self._path)

    def add(self, user: BaseUser):
        # if not passed_permit_check(self.get_current_user()):
        #     raise NotAuthorisedAccessError
        if self.search_by_mail(user.email) is None:
            self._db.loc[len(self._db.index)] = {"Name": user.name, "Password": user.password, "Role": user.role,
                                                 "Email": user.email, "Phone": user.phone}
            self._db["FirstName"] = self._db["Name"].apply(lambda x: x[0])
            self._db.sort_values(by=['FirstName'], inplace=True)
            self._db.drop(['FirstName'], axis=1, inplace=True)
            self._db.reset_index(drop=True, inplace=True)
        else:
            raise UserAlreadyExistError

    def remove_by_name(self, name: str):
        if not passed_permit_check(self.get_current_user()):
            raise NotAuthorisedAccessError
        found_user = self.search_by_name(name)
        if found_user == None:
            raise UserNotFoundError
        else:
            for elem in found_user:
                print("Found user:", elem)
                answer = input("Do You wont to remove this user? Y/N: ")
                while True:
                    if answer == 'Y' or answer=='y':
                        self._db.drop(elem.index, inplace=True)
                        print("user", name, "-deleted")
                        break
                    elif answer == 'N' or answer=='n':
                        break
                    else:
                        continue


    def remove_by_mail(self, mail: str):
        if not passed_permit_check(self.get_current_user()):
            raise NotAuthorisedAccessError
        found=self.search_by_mail(mail)
        # found = self._db.loc[self._db["Email"].str.contains(mail)]
        if found==None:
            print("Username Not found")
        else:
            print("Found user:", found)
            answer = input("Do You wont to remove this user? Y/N: ")
            while True:
                if answer == 'Y' or answer=='y':
                    self._db.drop(self._db.index[found.index])
                    print("user", found.email, "-deleted")
                    break
                elif answer == 'N' or answer=='n':
                    break
                else:
                    continue
    def remove_by_index(self, indx: int):
        if not passed_permit_check(self.get_current_user()):
            raise NotAuthorisedAccessError
        try:
            self._db.drop(indx, inplace=True)
            print("user with number", indx, "-deleted")
        except:
            raise IndexNotFoundError

    def search_by_name(self, name: str) -> List[BaseUser]:
        name = name.lower()
        self._db["FullName"] = self._db["Name"].apply(lambda x: " ".join(x))
        df = self._db.loc[self._db["FullName"].str.lower().str.contains(name)]
        df = df.loc[:, :"Phone"]
        self._db.drop(['FullName'], axis=1, inplace=True)
        found_user = []
        for index, elem in df.iterrows():
            found_user.append(
                BaseUser(elem["Name"], elem["Password"], elem["Role"], elem["Email"], elem["Phone"], index))
        if len(found_user) == 0: return None
        return found_user

    def search_by_mail(self, mail: str) -> BaseUser:
        mail = mail.lower()
        df = self._db.loc[self._db["Email"].str.lower().str.contains(mail)]
        # df.reset_index(drop=True, inplace=True)
        found_user = []
        for index, elem in df.iterrows():
            found_user.append(BaseUser(elem["Name"], elem["Password"], elem["Role"], elem["Email"], elem["Phone"],index))
        if not len(found_user):
            return None
        return found_user[0]

    @property
    def db(self):
        return self._db
class PartDataBase:
    def __init__(self, path: Path):
        if path.exists():
            self._path = path
            self._db = pd.DataFrame
            self.sync_init()
        else:
            raise DataFileError
    def sync_init(self):
        raise NotImplementedError

    def sync_shutdown(self):
        raise NotImplementedError

    def add(self, part: Part, db: UserDatabase):
        if not passed_permit_check(db.get_current_user()):
            raise NotAuthorisedAccessError
        try:
            self.search_by_code(part.code)
        except PartNotFoundError:
            self._db.loc[len(self._db.index)] = {"Code": part.code, "Name": part.name, "Category": part.category.name,
                                                 "Buy": part.buy_price, "Sell": part.sell_price, "Cars": part.list_of_cars}
            print("Part with code ", part.code, " successfully added")
            self._db.sort_values(by=['Code'], inplace=True)
            self._db.reset_index(drop=True, inplace=True)
        else:
            print("Part already exist")



    def search_by_name(self, name: str) -> List[Part]:
        name = name.lower()
        df = self._db.loc[self._db["Name"].str.lower().str.contains(name)]
        found_part = []
        if df.empty:
            print("Part not found")
            return None
        else:
            for index, elem in df.iterrows():
                found_part.append(
                    Part(elem["Code"], elem["Name"], elem["Category"], elem["Buy"], elem["Sell"], elem["Cars"]))
            # if len(found_part) == 0: return None
        return found_part

    def search_by_code(self, code_: int) -> Part:
        found = self._db.loc[self._db['Code'] == code_]
        found.reset_index(drop=True,inplace=True)
        if found.empty:
            print("Part not found")
            return None
        else:
            return Part(found.at[0, "Code"], found.at[0, "Name"], found.at[0, "Category"], found.at[0, "Buy"],
                    found.at[0, "Sell"], found.at[0, "Cars"])
    def remove_by_name(self, name: str, user_db: UserDatabase):
        if not passed_permit_check(user_db.get_current_user()):
            raise NotAuthorisedAccessError
        found_part = self.search_by_name(name)
        self._db = self._db.set_index('Code')
        if found_part is not None:
            for elem in found_part:
                print("Part:", elem)
                answer = input("Do You wont to remove this part? Y/N: ")
                if answer == 'Y' or answer=='y':
                    self._db.drop(elem.code, inplace=True)
                    print("part", name, "-deleted")
    def remove_by_code(self, code_: int, user_db: UserDatabase):
        if not passed_permit_check(user_db.get_current_user()):
            raise NotAuthorisedAccessError
        part_=self.search_by_code(code_)
        if part_ is not None:
            # self._db = self._db.set_index('Code')
            self._db.drop(labels=code_, inplace=True)
            print("part with code", code_, "-deleted")

    # def remove_by_index(self, indx: int, user_db: UserDatabase):
    #     if not passed_permit_check(user_db.get_current_user()):
    #         raise NotAuthorisedAccessError
    #     try:
    #         self._db.drop(indx, inplace=True)
    #         print("part with number", indx, "-deleted")
    #     except:
    #         print("Index not found")
    @property
    def db(self):
        return self._db
class BasketDatabase:
    _db=pd.DataFrame(index=None,columns=['UserName',"Ordered parts","Price"])

    @staticmethod
    def get_basket(user_name=UserDatabase.current_user.mail if UserDatabase.current_user else None):
        if not user_name:
            return BasketDatabase._db
        else:
            found=BasketDatabase._db.loc[BasketDatabase._db['UserName'].str.lower().str.contains(user_name)]
            found=found[['UserName','Ordered parts','Price']]
            if found.empty==False:return found
            else: return BasketDatabase._db

    @staticmethod
    def get_basket_price(user_name=UserDatabase.current_user.mail if UserDatabase.current_user else None):
        df=BasketDatabase.get_basket(user_name)
        if df.empty: raise UserNotFoundError
        sum=df['Price'].sum()
        return f"total price={sum}"

    @staticmethod
    def add_new_entry(part:Part):
        new_row={'UserName': UserDatabase.get_current_user().email if UserDatabase.get_current_user() is not None else None, 'Ordered parts': part.name,'Price':part.sell_price}

        # BasketDatabase._db=BasketDatabase._db.append(new_row,ignore_index=True)
        new_df=pd.DataFrame([new_row])
        if BasketDatabase._db.empty:BasketDatabase._db=new_df
        else: BasketDatabase._db=pd.concat([BasketDatabase._db,new_df],ignore_index=True)
        print(f"Parts Successfully added to {UserDatabase.get_current_user().email}'s basket")
        BasketDatabase._db.index+=1
        BasketDatabase._db.dropna(axis=1,inplace=True)
class CsvPartDataBase(PartDataBase):
    def sync_init(self):
        print('\nSynchronizing initial data from file...')
        self._db = pd.read_csv(self._path)

    def sync_shutdown(self):
        print('\nSynchronizing final data to file...')
        # print(self._db)
        self._db.to_csv(self._path,index=False)


