#Create a program that will ask how many apples and oranges you want to buy.
#Display the amount you need to pay if apple price is 20 pesos and orange is 25.

def Apple_Price():
    Apple_Func = int(20)
    return Apple_Func

def Orange_price():
    Orange_Func = int(25)
    return Orange_Func

def Display_Prices(ApplesF, OrangeF):
    print(f"The price for an apple is {ApplesF}, and the price for an orange is {OrangeF}.")

def Apple_Amount():
    Apple_Number = int(input("How many apples you want to buy: "))
    return Apple_Number

def Orange_Amount():
    Orange_Number = int(input("How many oranges you want to buy?: "))
    return Orange_Number

def Display_Amount(AppleA, OrangeA):
    print(f"The amount of apples bought is {AppleA} and the amount of oranges bought is {OrangeA} ")

def Calculate_Apple_Price():
    Apples_Prices = 20*Apple_Sum
    print(f"The total price of apples is {Apples_Prices}")
    return Apples_Prices

def Calculate_Orange_Price():
    Oranges_Prices = 25*Orange_Sum
    print(f"The total price of oranges is {Oranges_Prices}")
    return Oranges_Prices

def Total_Amount():
    Total = Apples_Prices + Oranges_Prices
    print(f"The total amount is {Total}")
    

# Steps:
# # 1. Present the apple and the orange price
Apples = Apple_Price()
Oranges = Orange_price()
Display_Prices(Apples, Oranges)
# 2. Ask how many apples and orange will buy
Apple_Sum = Apple_Amount()
Orange_Sum = Orange_Amount()
Display_Amount(Apple_Sum, Orange_Sum)
#Calculate the amount and price of apples and oranges
Apples_Prices = Calculate_Apple_Price()
Oranges_Prices = Calculate_Orange_Price()
#Give the total amount of apples and oranges combined
Total_Amount()