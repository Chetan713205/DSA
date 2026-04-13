from pydantic import BaseModel

class Person(BaseModel):
    name:str
    age:int
    city:str 

person=Person(name="Sumit Narayan", age=33, city="Bengaluru")
print(person)