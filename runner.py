from classes.bank import Bank

henderson_bank = Bank()


for i in range(12):
    print(vars(henderson_bank.accounts[i]))