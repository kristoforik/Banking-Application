import time, sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def account_num_checking(accounts, number):
    for n in range(len(accounts)):
            if accounts[n].accountNumber == number:
                return n

def check_negative(number):
    num = float(number)
    if num <= 0:
        num = input("Negative value cannot be processed. Enter the new value: ")
        num = check_amount(num)
    return num

def check_name(name):
    chname = str(name)
    while chname.isalpha() == False:
        chname = input("Enter a valid name: ")
    return chname

def check_inlist(alist, number):
    num = int(check_number(number))
    for i in alist:
        if str(num) == str(i.accountNumber):
            num = input("The number is not available. Enter the new one: ")
            num = check_inlist(alist, num)
    return num

def check_onetwothree(number):
    cnumber = str(number)
    while cnumber != '1' and cnumber != '2' and cnumber != '3':
        cnumber = input("Enter a valid number: ")
    return cnumber

def check_onetwo(number):
    cnumber = str(number)
    while cnumber != '1' and cnumber != '2':
        cnumber = input("Enter a valid number: ")
    return cnumber

def check_onetosix(number):
    cnumber = str(number)
    while cnumber != '1' and cnumber != '2' and cnumber != '3' and cnumber != '4' and cnumber != '5' and cnumber != '6':
        cnumber = input("Enter a valid number: ")
    return cnumber

def check_number(number):
    tnumber = str(number)
    cnumber = tnumber
    while cnumber.isnumeric() == False:
        cnumber = (input("Enter a valid number: "))
    return cnumber

def check_amount(amount):
    camount = amount
    while True:
        try:
            float(camount)
            camount = float(check_negative(camount))
            return camount
        except ValueError:
            camount = input("Enter a valid amount: ")

def creating_account(alist):
    print_slow("\u001b[36m---------Creating Account---------\u001b[0m\n")
    number = input("Enter the number for your account: ")
    number = int(check_number(number))
    number = check_inlist(alist, number)
    name = input("Enter your name: ")
    name = check_name(name)
    return Account(number, name, 0, 0, 0, 0, 0)

class Program:
    def run(self, account_list):
        print_slow("\u001b[36m---------\u001b[33mBank Application\u001b[36m---------\u001b[0m\n")
        time.sleep(1)
        self.showMainMenu(account_list)
    def showMainMenu(self, account_list):
        print_slow("\u001b[36m-------------Main Menu-------------\u001b[0m\n")
        print("[1] Open an account")
        print("[2] Select an account")
        print("[3] Exit the application")
        choice = (input("Enter the number: "))
        choice = int(check_onetwothree(choice))
        if choice == 1:
            time.sleep(0.5)
            newAcc = Bank()
            newAcc.openAccount(account_list)
        elif choice == 2:
            time.sleep(0.5)
            selAcc = Bank()
            selAcc.searchAccount(account_list)
        elif choice == 3:
            time.sleep(0.5)
            print("\u001b[31mYou left the application\u001b[0m")
            quit()
        else:
            print("Wrong")
    def showAccountMenu(self, account, account_list):
        print_slow("\u001b[36m------------\u001b[33mAccount Menu\u001b[36m------------\u001b[0m\n")
        print("Holder's name: ", account.getAccountHoldName())
        print("Holder's account number: ", account.getAccountNumber())
        print("Which account do you want to access?")
        print("[1] Checking account [2] Savings account")
        choice = (input("Enter the number: "))
        choice = int(check_onetwo(choice))
        if choice == 1:
            self.showCheqAccountMenu(account, account_list)
        elif choice == 2:
            self.showSavAccountMenu(account, account_list)
    def showCheqAccountMenu(self, account, account_list):
        print_slow("\u001b[36m-------\u001b[33mChequing Account Menu\u001b[36m-------\u001b[0m\n")
        print("What do you want to do?")
        print("[1] Check balance") 
        print("[2] Deposit money") 
        print("[3] Withdraw money") 
        print("[4] Exit to account menu")
        print("[5] Exit to main menu")
        print("[6] Exit the application")
        attempt = (input("Enter the number: "))
        attempt = int(check_onetosix(attempt))
        if attempt == 1:
            time.sleep(0.2)
            print(account.cheqaccount.getCurrentBalance())
            time.sleep(0.2)
            self.showCheqAccountMenu(account, account_list)
        elif attempt == 2:
            time.sleep(0.2)
            amount = input("Enter the amount to deposit: ")
            amount = float(check_amount(amount))
            account.cheqaccount.deposit(amount)
            print(account.cheqaccount.getCurrentBalance())
            time.sleep(0.5)
            print("\u001b[32mMoney successfully deposited\u001b[0m")
            time.sleep(0.5)
            self.showCheqAccountMenu(account, account_list)
        elif attempt == 3:
            amount = input("Enter the number to withdraw: ")
            amount = float(check_amount(amount))
            account.cheqaccount.withdraw(amount)
            time.sleep(0.5)
            self.showCheqAccountMenu(account, account_list)
        elif attempt == 4:
            time.sleep(0.5)
            self.showAccountMenu(account, account_list)
        elif attempt == 5:
            time.sleep(0.5)
            self.showMainMenu(account_list)
        elif attempt == 6:
            time.sleep(0.5)
            print("\u001b[31mYou left the application\u001b[0m")
            quit()
        else:
            print("Wrong")  
    def showSavAccountMenu(self, account, account_list):
        print_slow("\u001b[36m--------\u001b[33mSavings Account Menu\u001b[36m--------\u001b[0m\n")
        print("What do you want to do?")
        print("[1] Check balance") 
        print("[2] Deposit money") 
        print("[3] Withdraw money") 
        print("[4] Exit to account menu")
        print("[5] Exit to menu menu")
        print("[6] Exit the application")
        attempt = (input("Enter the number: "))
        attempt = int(check_onetosix(attempt))
        if attempt == 1:
            time.sleep(0.2)
            print(account.savaccount.getCurrentBalance())
            time.sleep(0.2)
            self.showSavAccountMenu(account, account_list)
        elif attempt == 2:
            time.sleep(0.2)
            amount = input("Enter the amount to deposit: ")
            amount = float(check_amount(amount))
            account.savaccount.deposit(amount)
            print(account.savaccount.getCurrentBalance())
            time.sleep(0.5)
            print("\u001b[32mMoney successfully deposited\u001b[0m")
            time.sleep(0.5)
            self.showSavAccountMenu(account, account_list)
        elif attempt == 3:
            amount = input("Enter the number to withdraw: ")
            amount = float(check_amount(amount))
            account.savaccount.withdraw(amount)
            time.sleep(0.5)
            self.showSavAccountMenu(account, account_list)
        elif attempt == 4:
            time.sleep(0.5)
            self.showAccountMenu(account, account_list)
        elif attempt == 5:
            time.sleep(0.5)
            self.showMainMenu(account_list)
        elif attempt == 6:
            time.sleep(0.5)
            print("\u001b[31mYou left the application\u001b[0m")
            quit()
        else:
            print("Wrong") 

class Bank:
    def __init__(self):
        self.bankName = 'CIBC'
    def openAccount(self, account_list):
        program = Program()
        tmp = creating_account(account_list)
        account_list.append(tmp)
        #print(account_list)
        time.sleep(0.5)
        program.showMainMenu(account_list)
    def searchAccount(self, account_list):
        menu = Program()
        print_slow("\u001b[36m---------Seleceting Account---------\u001b[0m\n")
        attempt = (input("Enter the account number: "))
        attempt = int(check_number(attempt))
        result = account_num_checking(account_list, attempt)
        if result == None:
            time.sleep(0.5)
            print("\u001b[31mThere is no account with such number\u001b[0m")
            time.sleep(0.5)
            menu.showMainMenu(account_list)
        else:
            user_account = account_list[result]
            time.sleep(0.5)
            menu.showAccountMenu(user_account, account_list)

class Account:
    def __init__(self, number, name, rate, sbalance, minbalance, cbalance, overdraft):
        self.accountNumber = number
        self.accountHoldName = name
        self.rateOfInterest = rate
        self.savaccount = SavingsAccount(sbalance, minbalance)
        self.cheqaccount = ChequingAccount(cbalance, overdraft)
    def getAccountNumber(self):
        return self.accountNumber
    def getAccountHoldName(self):
        return self.accountHoldName
    def getRateOfInterest(self):
        return self.rateOfInterest
    def withdraw(self):
        pass

class SavingsAccount():
    def __init__(self, sbalance, minbalance):
        self.balance = sbalance
        self.minimumBalance = minbalance
    def getCurrentBalance(self):
        return self.balance
    def withdraw(self, amount):
        if self.balance - amount <= self.minimumBalance:
            time.sleep(0.5)
            print("\u001b[31mUnfortunatelly, you cannot withdraw this amount because of the required minimum balance\u001b[0m")
            time.sleep(0.5)
            return self.balance
        else:
            self.balance -= amount
            time.sleep(0.5)
            print("\u001b[32mMoney successfully withdrawn\u001b[0m")
            time.sleep(0.5)
            return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
class ChequingAccount():
    def __init__(self, cbalance, overdraft):
        self.balance = cbalance
        self.overdraftAllowed = overdraft
    def getCurrentBalance(self):
        return self.balance
    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraftAllowed:
            self.balance -= amount
            time.sleep(0.5)
            print("\u001b[32mMoney successfully withdrawn\u001b[0m")
            time.sleep(0.5)
            return self.balance
        else:
            time.sleep(0.5)
            print("\u001b[31mUnfortunatelly, you cannot withdraw this amount as you exceed your overdraft limit\u001b[0m")
            time.sleep(0.5)
            return self.balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

# sbalance, minbalance, cbalance, overdraft
user1 = Account(100, 'John', 0, 4000, 1000, 2350.25, 2000)
user2 = Account(200, 'Mike', 0, 4000, 1000, 1934.40, 2000)
user3 = Account(300, 'Richard', 0, 4000, 1000, 65983.21, 2000)
user4 = Account(400, 'Andrew', 0, 4000, 1000, 15.90, 2000)
user5 = Account(500, 'Jason', 0, 4000, 1000, 159693.01, 2000)
accountList = [user1, user2, user3, user4, user5]

user = Program()
user.run(accountList)
