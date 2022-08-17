from pickle import TRUE
from User import user
from matplotlib import pyplot as plt
import matplotlib.pyplot as plotter
import numpy as np
import getpass


list_users = {}

def new_user():

    print("Create User_name")
    name = input()
    passwd=getpass.getpass("Create new password")   
    print("Enter Monthly Budget")
    budget = input()
    tname = name
    name = user(tname , budget , passwd, {})
    list_users[tname] = name

    print("User added")
   # pass

def verif(name, paswd):
    return list_users[name].verify( paswd)

def view_rem(name):
    if name in list_users:
        list_users[name].print_remain()
    else:
        print("User not found")

def add_expense(name):
    if len(list_users) == 0 or not(name in list_users):
        print("No existing users detected")
        pass
    else:
        detail = {}
        while True:
            i=int(input("1: Enter expense\n0:End\n"))
            if i==0:
                list_users[name].add_detail(**detail)
                return
            key=input("Enter category : ")
            value=input("Enter expense : ")
            detail[key]=value

def pie(name):
    if len(list_users) == 0 or not(name in list_users):
        print("No existing users detected")
        pass
    else:
        dat = []
        val = []
        for key,value in list_users[name]._detail:
            dat.append(key)
            val.append(value)
        figureObject, axesObject = plotter.subplots()

        axesObject.pie(val,

        labels=dat,

        autopct='%1.2f',

        startangle=90)


        axesObject.axis('equal')
        plotter.show()

        plt.show()



def main():

    while True:

        print("------------------Main Menu-----------------")
        print("1. Add new User")
        print("2. Add expenses")
        print("3: View remaining balance")
        print("4. Show chart representation")
        print("0. Exit")
        option = int(input())

        if option == 1:
            new_user()
        elif option == 2:
            n=input("Enter username : ")
            p=getpass.getpass("Enter password : ")
            if verif(n, p):
                add_expense(n)
            else:
                print("Wrong password!")
        elif option == 3:
            name=input("Enter username : ")
            p=getpass.getpass("Enter password : ")
            if verif(name, p):
                view_rem(name)
            else:
                print("Wrong password!")
        elif option == 4:
            name=input("Enter username : ")
            p=getpass.getpass("Enter password : ")
            if verif(name, p):
                pie(name)
            else:
                print("Wrong password!")
        elif option == 0:
            break
        else :
            print("Select valid Option")

if __name__ == '__main__':
    main()

