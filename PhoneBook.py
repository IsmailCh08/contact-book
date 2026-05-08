import json
import os

phone_Dict = {}
name = ""
number = ""
if os.path.exists('PhoneBook.json'):
    with open('PhoneBook.json', 'r') as file:
        phone_Dict = json.load(file)
else:
    phone_Dict = {}

def lookup_number():
    name = input("Whose number do you want to find? ")
    try:
        print(f"{name}'s number is {phone_Dict[name]}")
    except KeyError:
        print(f"{name} not found in the phonebook.")
    with open('PhoneBook.json', 'w') as file:
        json.dump(phone_Dict, file)

def edit_number():
    name = input("Whose number do you want to edit? ")
    while name not in phone_Dict.keys():
        print("Name doesnt exist")
        name = input("Whose number do you want to edit? ")
    number = input("What is their new number? ")
    phone_Dict[name] = number
    with open('PhoneBook.json', 'w') as file:
        json.dump(phone_Dict, file)


def delete_number():
    name = input("Whose number do you want to delete? ")
    try:
        phone_Dict.pop(name)
    except KeyError:
        print(f"{name} not found in the phonebook.")
    with open('PhoneBook.json', 'w') as file:
        json.dump(phone_Dict, file)

def insert_number(): 
    
    name = input("Whats the persons name? ")
    while name == '':
        print("Name cannot be empty!")
        name = input("Whats the persons name? ")

    number = input("Whats the persons number? ")
    while not number.isdigit():    
        number = input("Whats the persons number? ")

    phone_Dict[name] = number
    with open('PhoneBook.json', 'w') as file: 
        json.dump(phone_Dict, file)

option = input("What would you like to do today? Enter 1: to insert a number, Enter 2: delete a number, Enter 3: to lookup a number, Enter 4: to edit a number ")
option = int(option)
if option == 1:
    insert_number()
elif option == 2:
    delete_number()
elif option == 3:
    lookup_number()
elif option == 4:
    edit_number()