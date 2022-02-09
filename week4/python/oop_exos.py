
class Robot():
 	def __init__(self, name, color, weight):
 		self.name = name
 		self.color1 = color
 		self.weight = weight + 10

 	def introduce_self(self):
 		print(f'Hello im a robot and my name is {self.name} and i have the color {self.color1}')


class Person():
    def __init__(self, name, personnality, isSitting, robotOwned):
        self.name = name 
        self.personnality = personnality
        self.isSitting = isSitting
        self.robot = robotOwned
        self.hair = False

    def presentation(self):
        print(f'''Hi my name is {self.name}, \n
         i am very {self.personnality}\n 
         My robot is {self.robot.name} and
          he is {self.robot.color1}''')

    def sitDown(self):
        if self.isSitting == False:
            self.isSitting = True
            print(f'{self.name} is now sitting down')

    def standUp(self): 
        if self.isSitting :
            self.isSitting =False
            print(f'{self.name} is standing')

    def changeName(self, new_name):
        old_name= self.name
        self.name = new_name
        print(f'{old_name} is now called {self.name}')   
        

r1 = Robot('Tom', 'red', 65)
r2 = Robot('Jerry', 'blue', 40)

p1 = Person('Alice', 'aggressive', False, r2)
p2 =  Person('Becky', 'talkative', True, r1)

'''p1.sitDown()
print(p1.isSitting)

p2.presentation()

p1.presentation()

p1.changeName('Jane')
'''


class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance} fCFA")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


print('Creation de compte')
compte1 = BankAccount('Alice', 50147956348)
print(f'Congratulations {compte1.name}account created')

compte1.deposit(5000)
compte1.view_balance()

compte1.deposit(1000)
compte1.view_balance()
compte1.view_transactions()
