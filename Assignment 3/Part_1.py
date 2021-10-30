#Create a program that will ask for name, age and address.
#Display those details in the following format.
#Hi, my name is ________. I am ______ years old and I live in ______.

def Your_Name():
    Name = input("What is your name?: ")
    return Name

def Your_Age():
    Age = input("What is your age?: ")
    return Age

def Your_Address():
    Address = input("Where do you live?: ")
    return Address
def Display_Output(my_name, my_age, my_address):
    print(f"Hi, my name is {my_name}. I am {my_age} years old and I live in {my_address}.")

#Step
#1. Ask for users name
name = Your_Name()
#2. Ask for users age
age = Your_Age()
#3. Ask for users address
address = Your_Address()
#4. Present the output
Display_Output(my_name=name, my_age=age, my_address=address )