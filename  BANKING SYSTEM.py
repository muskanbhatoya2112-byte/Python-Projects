

account_numbers = [1001, 1002]

accounts = {
    1001: {"name": "Rahul", "balance": 5000},
    1002: {"name": "Priya", "balance": 8000}
}

class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Balance")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

def save_transaction(text):
    file = open("transactions.txt", "a")
    file.write(text + "\n")
    file.close()

try:
    acc_no = int(input("Enter Account Number: "))

    if acc_no in accounts:
        acc = BankAccount(
            acc_no,
            accounts[acc_no]["name"],
            accounts[acc_no]["balance"]
        )

        amount = float(input("Enter Deposit Amount: "))
        acc.deposit(amount)
        save_transaction(f"{acc_no} Deposited Rs.{amount}")

        amount = float(input("Enter Withdrawal Amount: "))
        acc.withdraw(amount)
        save_transaction(f"{acc_no} Withdrawn Rs.{amount}")

        print("Current Balance =", acc.check_balance())

    else:
        print("Account Not Found")

except Exception as e:
    print("Error:", e)