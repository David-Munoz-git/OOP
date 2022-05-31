
class BankAccount:
  all_accounts = []
  def __init__(self,interest_rate,balance):
    self.interest_rate = interest_rate
    self.balance = balance

    BankAccount.all_accounts.append(self)

  @classmethod 
  def get_all_accounts(cls):
    for account in cls.all_accounts:
      print(f"interest rate:{account.interest_rate} Balance: {account.balance}")
  
  @staticmethod
  def check_balance(self, amount):
    if (self.balance - amount) < 0:
      self.balance -= 50
      return False
    else:
      return True

BankAccount.get_all_accounts()


class User:
  all_user = []
  def __init__(self, data):
    self.name = data["name"]
    self.balance = data["balance"]
    self.checkings = BankAccount(4.0, 0)

    User.all_user.append(self)

  def deposit(self,amount):
    self.checkings.balance += amount
    print(self.checkings.balance)
    return self

  def make_withdrawl(self,amount):
    self.checkings.balance -= amount
    print(self.checkings.balance)
    return self

  def display_user_balance(self):
    print(f"User: {self.name}, Balance: {self.checkings.balance}")

    def transfer_money(self,amount,user):
      self.checkings.balance -= amount
      user.checkings.balance += amount
      print(f"You transfered money your balance is: {self.checkings.balance}")

adrien_data = {
    "name" : "Adrien Gold",
    "balance" : 0,
}
adrien = User(adrien_data)

nibbles_data = {
    "name" : "Mr. Nibbles",
    "balance" : 0,
}
nibbles = User(nibbles_data)
bob_data = {
    "name" : "Bob",
    "balance" : 0,
}
bob = User(bob_data)

adrien.deposit(200).deposit(200).deposit(100).make_withdrawl(50).display_user_balance()
nibbles.deposit(100).deposit(100).make_withdrawl(50).make_withdrawl(50).display_user_balance()
bob.deposit(2000).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_user_balance()
nibbles.transfer_money(200,adrien)
