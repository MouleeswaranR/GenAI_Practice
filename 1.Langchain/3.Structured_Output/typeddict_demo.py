from typing import TypedDict


#create a structure for dictionary about which keys and values should exist
class Person(TypedDict):
    name:str
    age:int

person:Person={'name':'raju','age':10}

print(person)