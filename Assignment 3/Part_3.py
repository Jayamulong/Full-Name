#Create a prgram which you will enter the amount of money you have, it will also ask for te price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.

def Money_Amount():
    money = float(input("Enter amount of money: "))
    return money

def Apple_Price():
    apple = float(input("Enter the price of an apple: "))
    return apple

def Sum():
    Apple_Amount = Money // Apple
    return Apple_Amount

def Money_Left():
    Amount = Total*Apple
    Change = Money - Amount
    return Change

def Display_Output(TotalA, ChangeM):
    print(f"You can buy {TotalA} apples and your change is {ChangeM:.2f} pesos.")


#Steps
#1. Ask how much money it have
Money = Money_Amount()
#2. Ask for price of an apple
Apple = Apple_Price()
#3. Calculate how many apples can buy in money
Total = Sum()
#4. Calculate how much change is left and 
Change = Money_Left()
#5. Report how many apples you can buy and your change
Display_Output(Total, Change)
