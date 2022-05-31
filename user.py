
class User:
  all_user = []
  def __init__(self, data):
    self.name = data["name"]
    self.balance = data["balance"]

    User.all_user.append(self)

  def deposit(self,amount):
    self.balance += amount
    print(self.balance)

  def make_withdrawl(self,amount):
    self.balance -= amount
    print(self.balance)

  def display_user_balance(self):
    print(f"User: {self.name}, Balance: {self.balance}")


  def transfer_money(self,other_user,amount):
    self.balance -= amount
    other_user.balance += amount
    print(f"Your transfered money your balance is: {self.balance}")


adrien_data = {
    "name" : "Adrien Gold",
    "balance" : 0,
}
adrien = User(adrien_data)

nibbles_data = {
    "name" : "Mr. Nibbles",
    "balance" : 500,
}
nibbles = User(nibbles_data)
bob_data = {
    "name" : "Bob",
    "balance" : 300,
}
bob = User(bob_data)

# adrien.deposit(200)
# adrien.deposit(200)
# adrien.deposit(100)
# adrien.make_withdrawl(50)
# adrien.display_user_balance()
# nibbles.deposit(100)
# nibbles.deposit(100)
# nibbles.make_withdrawl(50)
# nibbles.make_withdrawl(50)
# nibbles.display_user_balance()
# bob.deposit(2000)
# bob.make_withdrawl(25)
# bob.make_withdrawl(25)
# bob.make_withdrawl(25)
# bob.make_withdrawl(25)
# bob.display_user_balance()
nibbles.transfer_money(adrien,200)
