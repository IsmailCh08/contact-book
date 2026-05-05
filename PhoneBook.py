import json
import os

phone_Dict = {}
name = ""
number = ""
if os.path.exists('PhoneBook.json'):
    with open('phonebook.json', 'r') as file:
        phone_Dict = json.load(file)
else:
    phone_Dict = {}

def lookup_number(name):
    name = "Whose number do you want to find? "
    print(phone_Dict[name])


def delete_number(name):
    name = input("Whose name do you want to delete? ")
    phone_Dict.pop(name)
    with open('phonebook.json', 'w') as file:
        json.dump(phone_Dict, file)

def insert_number(name, number):  
    name = input("Whats the persons name? ")
    while type(name) != str :
        name = input("Whats the persons name? ")

    number = input("Whats the persons number? ")
    while not number.isdigit():    
        number = input("Whats the persons number? ")

    if name in phone_Dict:
        phone_Dict[name].append(number)  
    phone_Dict[name] = number
    with open('phonebook.json', 'w') as file: 
        json.dump(phone_Dict, file)

option = input("What would you like to do today? Enter 1: to insert a number, Enter 2: delete a number, Enter 3: to lookup a number: ")

if option == 1:
    insert_number()
elif option == 2:
    delete_number()
elif option == 3:
    lookup_number()