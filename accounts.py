from json import tool
from assetClasses import *

class Account:

    # an account contains a dictionary of assets with date and value
    # logger is a dictionary with key as date and value of a pair event and value
    def __init__(self):
        self.assets = {}
        self.logger = {}
        self.assets["Cash"] = []
        self.assets["Prepaid Expense"] = []
        self.assets["Accounts Receivable"] = []
        self.assets["Allowance for Doubtful Accounts"] = []
        self.assets["Bad Debt Expense"] = []
        self.totalAsset = 0 # holds the total value of assets

    # logger function to store transaction date, event and amount. Soon be changed into xlsx writer
    def log(self, date, event, amount):
        if date not in self.logger:
            self.logger[date] = []
        self.logger[date].append((event, amount))
    
    # a function that adds cash
    def addCash(self, amount):
        self.assets["Cash"].append(amount)
        self.log(amount.getDate(), "Debit Cash", amount.getValue())
        self.totalAsset += amount.getValue()
    
    # a function that adds prepaid expenses, will the same amount from cash
    def addPrepaid(self, amount):
        cash_change = Cash(-amount.getValue(), amount.getDate())
        self.assets["Prepaid Expense"].append(amount)
        self.assets["Cash"].append(cash_change)
        self.log(amount.getDate(), "Prepaid Expense", amount.getValue())
        self.log(amount.getDate(), "Debit Cash", -amount.getValue())
        self.totalAsset += amount.getValue()
    
    # a function that adds to accounts receivable
    def addAccountsReceivable(self, amount):
        self.assets["Accounts Receivable"].append(amount)
        self.log(amount.getDate(), "Accounts Receivable", amount.getValue())
        self.totalAsset += amount.getValue()
    
    # a function to help the user determine whether, a decrease in accounts receivable should go to cash,
    # allowance for doubtful accounts or bad debt expenses
    def changeAccountsReceivable(self, amount, date):
        is_doubtful = input("0 to Cash, 1 to Allowance for Doubtful Accounts, and 2 to Bad Debt Expense: ")
        self.log(date, "Accounts Receivable", -amount)
        if(is_doubtful == '0'):
            cash_change = Cash(amount, date)
            self.assets["Cash"].append(cash_change)
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
            self.log(date, "Debit Cash", amount)
        elif(is_doubtful == '1'):
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
            DA_change = allowance_for_doubtful_accounts(amount, date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
            self.log(date, "Allowance for Doubtful Accounts", amount)
        else:
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
            BDR_change = badDebtExpense(amount, date)
            self.assets["Bad Debt Expense"].append(BDR_change)
            self.log(date, "Bad Debt Expense", amount)
        
    # a function tohelp the user determine whether, a decrease in allowance for doubtful accounts should go to cash
    # or bad debt expenses
    def changeAllowanceForDoubtfulAccount(self, amount, date):
        is_doubtful = input("0 to Cash, and 1 to Bad Debt Expense: ")
        self.log(date, "Allowance for Doubtful Accounts", -amount)
        if(is_doubtful == '0'):
            cash_change = Cash(amount, date)
            self.assets["Cash"].append(cash_change)
            DA_change = allowance_for_doubtful_accounts(-(amount), date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
            self.log(date, "Debit Cash", amount)
        else:
            DA_change = allowance_for_doubtful_accounts(-(amount), date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
            BDR_change = badDebtExpense(amount, date)
            self.assets["Bad Debt Expense"].append(BDR_change)
            self.log(date, "Bad Debt Expense", amount)
            
    # a function to show all assets with their respective transaction.
    # final print is the total value of assets
    def showAllAssets(self):
        print()
        print()
        for i in self.assets.keys():
            retval = 0
            toPrint = self.assets[i]
            print(i,": ")
            for j in range(len(toPrint)):
                retval += toPrint[j].getValue()
                print(toPrint[j].date, " ", toPrint[j].getValue())
            print("Total Amount: ", retval)
            print("_______________________________")
        print("Total Assets: ",self.totalAsset)
        print()

    # a function to show all transaction information based on date
    def showLog(self):
        print()
        print()
        for i in self.logger.keys():
            to_print = self.logger[i]
            print(i, end =": ")
            print(to_print[0][0], " ", to_print[0][1])
            if(len(to_print) > 1):
                for j in range(1, len(to_print)):
                    print("           ", to_print[j][0], " ", to_print[j][1])
            print("__________________________________________________________")
            print()