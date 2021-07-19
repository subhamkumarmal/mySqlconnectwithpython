from functions.mainclass import MysqlConnectivity
from connections.connection import createConnection


def task1():
    obj = MysqlConnectivity()
    tableName=input("Enter the tabe that you want to create : ")
    sizes = int(input("Enter the size of the column : "))
    lst=[]
    for i in range(sizes):
        columns=input("Enter the column name with varable : ")
        lst.append(columns)
    obj.createTables(tableName,lst)


def task2():
    obj=MysqlConnectivity()
    tname=input("Enter the table name for reading the data from the database : ")
    take=obj.descriptions(tname)
    obj.read(tname,take)


def task3():
    obj = MysqlConnectivity()
    tname=input("Enter the table name where you want to insert the data :")
    dataSize = int(input("Enter the size that you want to store the data : "))
    fields = obj.descriptions(tname)
    for i in range(dataSize):
        lst = []
        for j in fields:
            value = input(f"Enter the {j} : ")
            lst.append(value)

        obj.insertData(tname,lst)

def task4():
    tname=input("Enter the table name from where you want to delete :")
    names=input("Enter table column name by which you element will be deleted.")
    keys=input("Enter the row keys that you want to delete : ")
    obj=MysqlConnectivity()
    obj.delete(tname,names,keys)

def task5():
    obj=MysqlConnectivity()
    tname=input("Enter the table name which you want to drop from the database : ")
    obj.dropTable(tname)


