class time:
    def __init__(self, hours, day):
        self.hours = hours
        self.day = day

class money:
    def __init__(self, cash, checking_balance, savings_balance):
        self.cash = cash
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

class job:
    def __init__(self, salary):
        self.salary = salary

class interest:
    def __init__(self, saving_interest_earned,saving_daily_rate_interest, checking_interest_earned, checking_daily_rate_interest):
        self.saving_interest_earned = saving_interest_earned
        self.saving_daily_rate_interest = saving_daily_rate_interest
        self.checking_interest_earned = checking_interest_earned
        self.checking_daily_rate_interest = checking_daily_rate_interest

mon = money(500,0,0)
tm = time(6,0)
jb = job
intrs = interest
def checking_account_deposit():
    print("How much money do you like to deposit into checking account")
    action = int(input(">"))
    if action <= mon.cash:
        mon.cash -= action
        mon.checking_balance += action
        bank()
    elif action > mon.cash:
        print("Don't have enough cash")
        bank()

def checking_account_to_savings_account():
    print("How much money do you want to move into saving balance:")
    action = int(input(">"))
    if action <= mon.checking_balance:
        mon.checking_balance -= action
        mon.savings_balance += action
        print("Your checking balance:", mon.checking_balance)
        print("Your savings balance:", mon.savings_balance)
        bank()
    elif action > mon.checking_balance:
        print("You don't have that amount of money")
        bank()

def savings_account_to_checking_account():
    print("How much money do you want to move into checking balance")
    action = float(input(">"))
    if action <= mon.savings_balance:
        mon.savings_balance -= action
        mon.checking_balance += action
        print("Your checking balance:", mon.checking_balance)
        print("Your saving balance:", mon.savings_balance)
        bank()
    elif action > mon.savings_balance:
        print("You don't have that amount of money")
        bank()

def savings_interest():
    intrs.saving_daily_rate_interest = 0.005
    intrs.saving_interest_earned = mon.savings_balance * intrs.saving_daily_rate_interest
    if mon.savings_balance > 0:
        mon.savings_balance += intrs.saving_interest_earned
    
    
def checking_interest():
    intrs.checking_daily_rate_interest = 0.001
    intrs.checking_interest_earned = mon.checking_balance * intrs.checking_daily_rate_interest
    if mon.checking_balance > 0:
        mon.checking_balance += intrs.checking_interest_earned
    
def working():
    print("How long do you work?")
    answer = int(input(">"))
    if answer <= 24:
        jb.salary = answer * 15
        tm.hours += answer
        print("You're working for", answer,"hours")
        mon.checking_balance += jb.salary
    else:
        print("pls input hours not exceed 24 hours")
        working()
    world_map()

def withdraw_money():
    print("How much money do you want to withdraw?")
    answer = int(input(">"))
    if answer <= mon.checking_balance:
        mon.checking_balance -= answer
        mon.cash += answer
        print("Your cash balance:", mon.cash)
        print("Your Checking balance:", mon.checking_balance)
        bank()
    elif answer > mon.checking_balance:
        print("You don't have that amount of money")
        bank()
def time_moving():
    if tm.hours >= 24:
        tm.hours -= 24
        tm.day += 1
        savings_interest()
        checking_interest()

def bank():
    time_moving()
    print("Days:", tm.day)
    print("hours", tm.hours)
    print("checking balance:", mon.checking_balance)
    print("savings balance:", mon.savings_balance)
    print("cash:", mon.cash)
    print("What do you want to do?")
    print("1.Deposit checking account")
    print("2.Moving Account")
    print("3.Withdraw")
    print("4.to world map")
    answer = int(input(">"))
    if answer == 1:
        checking_account_deposit()
    elif answer == 2:
        print("1. checking account to deposit account")
        print("2. deposit account to checking account")
        answer = int(input(">"))
        if answer == 1:
            checking_account_to_savings_account()
        elif answer == 2:
            savings_account_to_checking_account()
    elif answer == 3:
        withdraw_money()
    elif answer == 4:
        world_map()

def world_map():
    time_moving()
    print("Days:", tm.day)
    print("hours", tm.hours)
    print("checking balance:", mon.checking_balance)
    print("savings balance:", mon.savings_balance)
    print("cash:", mon.cash)
    print("What do you want to do?")
    print("1.Home")
    print("2.Bank")
    print("3.working")
    print("4.skip days")
    print("5. exit game")
    answer = int(input(">"))
    if answer == 1:
        print("Do you want to sleep(1) or take a nap(2)?")
        answer = int(input(">"))
        if answer == 1:
            tm.hours += 8
        elif answer == 2:
            tm.hours += 4
        world_map()
    if answer == 2:
        if tm.hours >= 8 and tm.hours <= 15:
            bank()
        else:
            print("Bank Closed, come tommorow")
            world_map()
    if answer == 3:
        working()
    if answer == 4:
        tm.hours += 24
        world_map()
    if answer == 5:
        exit(0)
    else:
        print("input right option")
        world_map()

world_map()
