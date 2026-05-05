import json
import os

phone_Dict = {}

if os.path.exists('PhoneBook.json'):
    with open('phonebook.json', 'r') as file:
        phone_Dict = json.load(file)
else:
    phone_Dict = {}

name = input("Whats the persons name? ")
while type(name) != str :
    name = input("Whats the persons name? ")

number = input("Whats the persons number? ")
while not number.isdigit():    
    number = input("Whats the persons number? ")

def insert_number(name, number):  
    if name in phone_Dict:
        phone_Dict[name].append(number)  
    phone_Dict[name] = number
    with open('phonebook.json', 'w') as file: 
        json.dump(phone_Dict, file)
insert_number(name,number)
print(phone_Dict)