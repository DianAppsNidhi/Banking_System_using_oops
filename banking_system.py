class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("!!...User's Detail...!!")    
        print(self.name)
        print(self.age)
        print(self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your total balance : ", self.balance)

    def withdrawl(self, amount):
        self.amount = amount
        if self.balance > self.amount:
            print("You have not enough balance")
        else:
            self.balance = self.balance - self.amount
            print("You withdrawl : ", self.amount , "\nYour balance amount is : ", self.balance) 

    def view_balance(self):
        self.show_details()
        print("Your available balance : ",self.balance)

user1 = User("Nidhi", 20, "Female")
# user1.show_details() 
bank = Bank("Nidhi", 20, "Female") 
# bank.deposit(5000)


# bank.withdrawl(3000)

# bank.view_balance() 

# bank.deposit(5000)

bank.withdrawl(1000)


          