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

def check_onetwo(number):
    tnumber = str(number)
    cnumber = tnumber
    while cnumber.isnumeric() == False and cnumber == '1' or cnumber == '2':
        cnumber = (input("Enter a valid number: "))
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
            return camount
        except ValueError:
            camount = input("Enter a valid amount: ")

def creating_account():
    number = input("Enter the number for your account: ")
    number = int(check_number(number))
    name = input("Enter your name: ")
    name = check_name(name)
    return Account(number, name, 0, 0, 0, 0, 0)

class Program:
    def run(self, account_list):
        self.showMainMenu(account_list)
    def showMainMenu(self, account_list):
        print("[1] Open an account")
        print("[2] Select an account")
        print("[3] Exit the application")
        choice = (input("Enter the number: "))
        choice = int(check_number(choice))
        if choice == 1:
            newAcc = Bank()
            newAcc.openAccount(account_list)
        elif choice == 2:
            selAcc = Bank()
            selAcc.searchAccount(account_list)
        elif choice == 3:
            quit()
        else:
            print("Wrong")
    def showAccountMenu(self, account, account_list):
        print("Holder's name: ", account.getAccountHoldName())
        print("Holder's account number: ", account.getAccountNumber())
        print("Which account do you want to access?")
        print("[1] Checking account [2] Savings account")
        choice = int(input("Enter the number: "))
        if choice == 1:
            self.showCheqAccountMenu(account, account_list)
        elif choice == 2:
            self.showSavAccountMenu(account, account_list)
    def showCheqAccountMenu(self, account, account_list):
        print("What do you want to do?")
        print("[1] Check balance") 
        print("[2] Deposit money") 
        print("[3] Withdraw money") 
        print("[4] Exit to account menu")
        print("[5] Exit to main menu")
        print("[6] Exit the application")
        attempt = int(input("Enter the number: "))
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
            print("Money successfully deposited")
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
            print("You left the application")
            quit()
        else:
            print("Wrong")  
    def showSavAccountMenu(self, account, account_list):
        print("What do you want to do?")
        print("[1] Check balance") 
        print("[2] Deposit money") 
        print("[3] Withdraw money") 
        print("[4] Exit to account menu")
        print("[5] Exit to menu menu")
        print("[6] Exit the application")
        attempt = int(input("Enter the number: "))
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
            print("Money successfully deposited")
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
            print("You left the application")
            quit()
        else:
            print("Wrong") 

class Bank:
    def __init__(self):
        self.bankName = 'CIBC'
    def openAccount(self, account_list):
        program = Program()
        tmp = creating_account()
        account_list.append(tmp)
        #print(account_list)
        program.showMainMenu(account_list)
    def searchAccount(self, account_list):
        attempt = int(input("Enter the account number: "))
        result = account_num_checking(account_list, attempt)
        if result == None:
            print("Wrong number")
        else:
            user_account = account_list[result]
            account_menu = Program()
            account_menu.showAccountMenu(user_account, account_list)

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
    '''def getCurrentSavingsBalance(self):
        return self.currentBalance
    def getCurrentChequingBalance(self):
        return self.currentBalance
    def deposit(self, amount):
        self.currentBalance = self.currentBalance + amount
        return self.currentBalance'''
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
            print("Unfortunatelly, you cannot withdraw this amount because of the required minimum balance")
            return self.balance
        else:
            self.balance -= amount
            print("Money successfully withdrawn")
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
            print("Money successfully withdrawn")
            return self.balance
        else:
            print("Unfortunatelly, you cannot withdraw this amount as you exceed your overdraft limit")
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
user.run(accountList)
