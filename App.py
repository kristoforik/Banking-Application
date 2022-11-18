import time
'''account_numbers = [100, 200, 300, 400, 500]
accounts = {
    100 : [100, 'John', 0, 2400.25]
}
nu = 100
def account_check(accounts_numbers, number):  
    for n in range(len(accounts_numbers)):
        if accounts_numbers[n] == number:
            return n
tmp = account_check(account_numbers, nu)
acc = account_numbers[tmp] '''
def account_num_checking(accounts, number):
    for n in range(len(accounts)):
            if accounts[n].accountNumber == number:
                return n

def check_name(name):
    chname = str(name)
    while chname.isalpha() == False:
        chname = input("Enter a valid name: ")
    return chname

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
            return camount
        except ValueError:
            camount = input("Enter a valid product price: ")

def creating_account():
    number = input("Enter the number for your account: ")
    number = check_number(number)
    name = input("Enter your name: ")
    name = check_name(name)
    return Account(number, name, 0, 0)

class Program:
    def run(self):
        self.showMainMenu()
    def showMainMenu(self):
        print("[1] Open an account")
        print("[2] Select an account")
        print("[3] Exit the application")
        choice = (input("Enter the number: "))
        choice = int(check_number(choice))
        if choice == 1:
            newAcc = Bank()
            newAcc.openAccount()
        elif choice == 2:
            selAcc = Bank()
            selAcc.searchAccount()
        elif choice == 3:
            quit()
        else:
            print("Wrong")
    def showAccountMenu(self, account):
        print("Holder's name: ", account.getAccountHoldName())
        print("Holder's account number: ", account.getAccountNumber())
        print("What do you want to do?")
        print("[1] Check balance") 
        print("[2] Deposit money") 
        print("[3] Withdraw money") 
        print("[4] Exit to main menu")
        print("[5] Exit the application")
        attempt = int(input("Enter the number: "))
        if attempt == 1:
            print(account.getCurrentBalance())
            time.sleep(0.5)
            print("[1] Exit to account menu")
            print("[2] Exit to main menu")
            print("[3] Exit the application")
            choice = int(input("Enter the number: "))
            if choice == 1:
                self.showAccountMenu(account)
            elif choice == 2:
                self.showMainMenu()
            elif choice == 3:
                quit()
        elif attempt == 2:
            amount = input("Enter the amount to deposit: ")
            amount = float(check_amount(amount))
            account.deposit(amount)
            print(account.getCurrentBalance())
            time.sleep(0.5)
            print("Money successfully deposited")
            time.sleep(0.5)
            self.showAccountMenu(account)
        elif attempt == 3:
            print("You withdrawed")
        elif attempt == 4:
            time.sleep(0.5)
            self.showMainMenu(account)
        elif attempt == 5:
            time.sleep(0.5)
            print("You left the application")
            quit()
        else:
            print("Wrong")
        return account

class Bank:
    def __init__(self):
        user1 = Account(100, 'John', 0, 2350.25)
        user2 = Account(200, 'Mike', 0, 1934.40)
        user3 = Account(300, 'Richard', 0, 65983.21)
        user4 = Account(400, 'Andrew', 0, 15.90)
        user5 = Account(500, 'Jason', 0, 159693.01)
        self.bankName = 'CIBC'
        self.account_list = [user1, user2, user3, user4, user5]
    def openAccount(self):
        tmp = creating_account()
        self.account_list.append(tmp)
        print(self.account_list[-1].accountHoldName)
        return self.account_list
    def searchAccount(self):
        attempt = int(input("Enter the account number: "))
        result = account_num_checking(self.account_list, attempt)
        if result == None:
            print("Wrong number")
        else:
            user_account = self.account_list[result]
            account_menu = Program()
            account_menu.showAccountMenu(user_account)

class Account:
    def __init__(self, number, name, rate, balance):
        self.accountNumber = number
        self.accountHoldName = name
        self.rateOfInterest = rate
        self.currentBalance = balance
    def getAccountNumber(self):
        return self.accountNumber
    def getAccountHoldName(self):
        return self.accountHoldName
    def getRateOfInterest(self):
        return self.rateOfInterest
    def getCurrentBalance(self):
        return self.currentBalance
    def deposit(self, amount):
        self.currentBalance = self.currentBalance + amount
        return self.currentBalance
    def withdraw(self):
        pass

class SavingsAccount(Account):
    def __init__(self, number, name, rate, balance):
        super().__init__(number, name, rate, balance)
        self.minimumBalance = 0
    def withdraw(self):
        pass
    
class SavingsAccount(Account):
    def __init__(self, number, name, rate, balance):
        super().__init__(number, name, rate, balance)
        self.overdraftAllowed = 0
    def withdraw(self):
        pass

class CreditScore(Account):
    def __init__(self, number, name, rate, balance):
        super().__init__(number, name, rate, balance)
        self.credit_score = 0





'''a = accounts[0]
print(a[0])

user1 = Account(100, 'John', 0, 2350.25)
user2 = Account(200, 'Mike', 0, 1934.40)
user3 = Account(300, 'Richard', 0, 65983.21)
user4 = Account(400, 'Andrew', 0, 15.90)
user5 = Account(500, 'Jason', 0, 159693.01)
accounts = [user1, user2, user3, user4, user5]'''

#bank = Bank()
#print(bank.account_list[1].getAccountNumber())


user = Program()
user.run()
