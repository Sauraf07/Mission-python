class BankAccount:
    bank_name:"Dragon_Bank"
    total_accounts = 0

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    def show_balance(self):
        print(f"{self.owner} ka balance : Rs:{self.balance}")

    def bank_info(cls):
        print(f"Bank: {cls.bank_name}")
        print(f"Total Accounts:{cls.total_accounts}")

    def Is_valid_depost(amount):
        if amount > 0:
            return  "valid amount"
        else:
            return "invalid Amount"

acc1 = BankAccount("Saurav",5000)
acc2 = BankAccount("Priyam",5000)

acc1.show_balance()
BankAccount.bank_info()
print(BankAccount.Is_valid_depost(500))
print(BankAccount.Is_valid_depost(-100))