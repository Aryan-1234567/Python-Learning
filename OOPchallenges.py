#challenge 1

class BankAccount: 
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. new balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient amount')
        else:
            self.balance = self.balance - amount

    def display_balance(self):
        print(f' Balance: {self.balance}')

#example 2
class CricketPlayer:
    def __init__ (self, name, runs, wickets):
        self.name = name
        self.runs = runs
        self.wickets = wickets

        def score_runs(self, amount):
            self.runs += amount
            print(f"{self.name} score {amount} runs. ")

        def take_wicket(self):
            self.wickets += 1
            print(f' {self.name} took {self.wickets} wickets. ')

        def display_stats(self):
            print(f'Player: {self.name}, Runs: {self.runs}, Wickets: {self.wickets}')

#example 3
class Vehicle:
    def __init__ (self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} accelerates by {self.amount}")

    