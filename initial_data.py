"""
This program creates initial UserDataBase and PartDataBase and safes the data into
parts.csv and users.pickle
"""


import pandas as pd
from part import Part,PartsCategory
from user import BaseUser, AdminUser,User
from pathlib import Path

data_parts=[
    Part(1111,"Bonnet/hood",PartsCategory.TRUCK,110,120,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(1122,"Bumper",PartsCategory.TRUCK,80,82,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(1133,"Cowl screen",PartsCategory.TRUCK,55,60,["BMW 316i, 1992","Mitsubishi Pajero, 2005", "Opel Corsa, 1997"]),
    Part(1144,"Decklid",PartsCategory.TRUCK,115,118,["Suzuki vitara, 2002","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(1155,"Fender",PartsCategory.TRUCK,88,90,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(2211,"Grille (also called grill)",PartsCategory.ENGINE,160,162,["BMW 316i, 1992","Ford Fiesta, 1995", "Mitsubishi Pajero, 2005"]),
    Part(2222,"Pillar and hard trim",PartsCategory.ENGINE,104,108,["Suzuki vitara, 2002","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(2233,"Radiator core support",PartsCategory.ENGINE,111,112,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(2244,"Quarter panel",PartsCategory.ENGINE,122,133,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(2255,"Hubcap",PartsCategory.ENGINE,131,132,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(3311,"Camshaft locking plate",PartsCategory.WHEELS,55,65,["BMW 316i, 1992","Mitsubishi Pajero, 2005", "Opel Corsa, 1997"]),
    Part(3322,"Connecting rod washer",PartsCategory.WHEELS,72,74,["Mitsubishi Pajero, 2005, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(3333,"Crank case",PartsCategory.WHEELS,25,27,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(3344,"Distributor cap",PartsCategory.WHEELS,78,82,["BMW 316i, 1992","Suzuki vitara, 2002", "Opel Corsa, 1997"]),
    Part(3355,"Distributor cap",PartsCategory.WHEELS,76,84,["Mitsubishi Pajero, 2005, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(4421,"Drive belt",PartsCategory.ACCESSORIES,14,18,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(4431,"Starter ring",PartsCategory.ACCESSORIES,101,105,["BMW 316i, 1992","Ford Fiesta, 1995", "Suzuki vitara, 2002"]),
    Part(4431,"Water pump gasket",PartsCategory.ACCESSORIES,120,122,["BMW 316i, 1992","Ford Fiesta, 1995", "Opel Corsa, 1997"]),
    Part(4441,"Air spring",PartsCategory.ACCESSORIES,45,48,["BMW 316i, 1992","Suzuki vitara, 2002", "Mitsubishi Pajero, 2005"]),
    ]
dict_parts_data=[]
for part in data_parts:
    dict_parts_data.append({"Code":part.code,"Name":part.name,"Category":part.category.name,
                      "Buy":part.buy_price,"Sell":part.sell_price,"Cars":part.list_of_cars})
pd.set_option("display.max_columns", 20)
pd.set_option('expand_frame_repr', False)
if not Path("parts.csv").exists():
    df_parts=pd.DataFrame(dict_parts_data)
    df_parts.to_csv("parts.csv",index_label="Code",index=False)
    db_parts=pd.read_csv("parts.csv")
    print(db_parts)
data_users=[
    User(["Ivan","Petrov"],"ip1102","ivan@abv.bg","0887324776"),
    User(["Dragan","Petkanov","Draganov"],"dr3324","dragan@abv.bg","0543887646"),
    User(["Dimo","Petkov"],"dm3352","dimo@abv.bg","0885226776"),
    User(["Plamen","Kostov"],"pl7737","plamen@abv.bg","0665447887"),
    User(["Kiril","Donchev"],"kiro4432","donchev@abv.bg","0883223344"),
    AdminUser(["Koko","Penchev"],"kiki0944","koko@abv.bg","0886333245"),
    AdminUser(["Aneta","Franklin"],"ani4432","ana@abv.bg","0888448392")
]
dict_users_data=[]
for user in data_users:
    dict_users_data.append({"Name":user.name,"Password":user.password,"Role":user.role,
                            "Email":user.email,"Phone":user.phone})
if not Path("users.pickle").exists():
    df_users=pd.DataFrame(dict_users_data)
    df_users.to_pickle("users.pickle")
    db_users=pd.read_pickle("users.pickle")
    print(db_users)
