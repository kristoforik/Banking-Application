
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

class Program:
    def run(self):
        self.showMainMenu()
    def showMainMenu(self):
        print("[1] Open an account")
        print("[2] Select an account")
        print("[3] Exit the application")
        choice = int(input("Enter the number: "))
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
    def showAccountMenu(self):
        pass

class Bank:
    def __init__(self):
        self.bankName = 'CIBC'
    def openAccount(self):
        pass
    def searchAccount(self):
        attempt = int(input("Enter the account number: "))
        result = account_num_checking(accounts, attempt)
        if result == None:
            print("Wrong number")
        else:
            print(accounts[result].accountHoldName)
            

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
    def deposit(self):
        pass
    def withdraw(self):
        pass

class SavingsAccount:
    def __init__(self):
            self.minimumBalance = 0
    def withdraw(self):
        pass
    
class SavingsAccount:
    def __init__(self):
            self.overdraftAllowed = 0
    def withdraw(self):
        pass


'''a = accounts[0]
print(a[0])'''

user1 = Account(100, 'John', 0, 2350.25)
user2 = Account(200, 'Mike', 0, 1934.40)
user3 = Account(300, 'Richard', 0, 65983.21)
user4 = Account(400, 'Andrew', 0, 15.90)
user5 = Account(500, 'Jason', 0, 159693.01)
accounts = [user1, user2, user3, user4, user5]




user = Program()
user.run()
