class time:
    def __init__(self,hours,days,bank_deposit_days):
        self.hours = hours
        self.days = days
        self.bank_deposit_days = bank_deposit_days
class money:
    def __init__(self,money,salary):
        self.money = money
        self.salary = salary

class bank:
    def __init__(self, deposit,apr,interest):
        self.deposit = deposit
        self.apr = apr
        self.interest = interest

t1 = time(6, 0, 0)
b1 = bank(0,0,0)
pro = money(100, 5)
def days():
    if t1.hours > 24:
        t1.days +=1
        t1.hours -= t1.hours
        if(b1.deposit > 0):
            t1.bank_deposit_days +=1
        else:
            t1.bank_deposit_days = 0
days()
def bankdeposit():
    answer = int(input("Hello Sir, How much do you want to deposit the money?"))
    if pro.money < answer:
        print("you don't have any cash")
    else:
        pro.money -= answer
        b1.deposit += answer
    banks()
def calculate_interest():
    if (b1.deposit > 0 and t1.bank_deposit_days >= 1):
        b1.apr = 0.10
        b1.interest = b1.apr / 365
        b1.deposit = b1.deposit + b1.interest
        t1.bank_deposit_days -= 1
    if(b1.deposit > 0 and t1.bank_deposit_days < 1):
        b1.deposit = b1.deposit + b1.interest
def working():
    if (t1.hours < 8 or t1.hours > 16 ):
        print("The workplace is closed")
        main()
    else:
        print("Start Working")
        t1.hours +=8
        pro.money = pro.money + (pro.salary * 8)
        main()

def deep_sleep():
    print("ZZZZZZZZZZZZZZZZZZZZZZ")
    t1.hours += 8
    main()
def nap():
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzz")
    t1.hours += 4
    main()

def home():
    print("Do you want to sleep(1) or nap(2)?")
    answer = int(input(">"))
    if(answer == 1):
        deep_sleep()
    if(answer == 2):
        nap()
def check_balance():
    calculate_interest()
    print("Your bank balance is", b1.deposit, "$")
    banks()

def withdraw():
    print("how much money do you want to withdraw?")
    answer = int(input(">"))
    answer -= b1.deposit
    answer += pro.money
    if (b1.deposit == 0):
        print("You don't have money in your bank account")
        banks()

def banks():
    print("What do you want to do?")
    print("1. check balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. bank to main option")
    answer = int(input(">"))
    if (answer == 1):
        check_balance()
    if (answer == 2):
        bankdeposit()
    if (answer == 3):
        withdraw()
    if (answer == 4):
        t1.hours += 1
        main()

def main():
    days()
    print("Days:", t1.days)
    print("time",t1.hours, "O'clock")
    print("Cash:",pro.money,"$")
    print("where do you want to go")
    print("1. Go to the workplace")
    print("2. Go to the bank")
    print("3. Go to the house")
    answer = int(input(">"))
    if (answer == 1):
        working()
    if (answer == 2):
        banks()
    if (answer == 3):
        home()
    else:
        print("input the right option")

main()

