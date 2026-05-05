import json

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

insert_number(name,number)
print(phone_Dict)