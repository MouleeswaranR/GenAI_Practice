from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):

    name:str='raju'
    age:Optional[int]=None
    email:EmailStr#built-in validation for email
    cgpa:float=Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of a student') #adding constarints to a field(greater than 0 and less than 10)

# new_student={'name':'raju'}

# new_student={'age':20}#uses default values

# new_student={'age':'20'}#pydantic will parse str 20 to int 20 implicitly

#new_student={'age':'20','email':'abc'}#raise error because email is not valid email string(validates internally because of EmailStr from pydantic)
new_student={'age':'20','email':'abc@gmail.com'}

student=Student(**new_student)

print(student)
print(type(student))
print(student.name)

student_dict=dict(student)
print(student_dict['age'])

student_json=student.model_dump_json()
print(student_json)
#if datatype for any key's value is different from defined class, raised error at runtime
#if in place of str, int is used , raise error which is not available in typeddict
