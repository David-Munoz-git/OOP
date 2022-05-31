
class BankAccount:
  all_accounts = []
  def __init__(self, data):
    self.interest_rate = data["interest rate"]
    self.balance = data["balance"]

    BankAccount.all_accounts.append(self)

  @classmethod 
  def get_all_accounts(cls):
    for account in cls.all_accounts:
      print(f"interest rate:{account.interest_rate} Balance: {account.balance}")
  
  @staticmethod
  def check_balance(self, amount):
    if (self.balance - amount) < 0:
      self.balance -= 5
      return False
    else:
      return True

  def deposit(self, ammount):
    self.balance += ammount
    print(f"Balance: {self.balance}")
    return self
  def withdraw(self,amount):
      if self.check_balance(self,amount):
        self.balance -= amount
        print(f"Balance: {self.balance}")
        return self
      else:
        print("Unsufficent Funds, Over draff fee is $50")
        return self
  def display_account_info(self):
    print(f'Your balance is: {self.balance}')
    return self
  def yield_interest(self):
    self.balance = self.interest_rate * self.balance + self.balance
    print(f"Balance after interest rate is: {self.balance}")
    return self

adam_data = {
  "interest rate" : 0.01,
  "balance" : 0,
}
adam = BankAccount(adam_data)


sams_data = {
  "interest rate" : 0.01,
  "balance" : 500,
}
sams = BankAccount(sams_data)


adam.deposit(100).deposit(200).deposit(100).withdraw(400).display_account_info().yield_interest()


sams.deposit(100).deposit(200).withdraw(10).withdraw(20).withdraw(30).withdraw(50).display_account_info().yield_interest()

BankAccount.get_all_accounts()
