from faulthandler import cancel_dump_traceback_later
from assetClasses import *

class Account:
    def __init__(self):
        self.assets = {}
        self.assets["Cash"] = []
        self.assets["Prepaid Expense"] = []
        self.assets["Accounts Receivable"] = []
        self.assets["Allowance for Doubtful Accounts"] = []
        self.assets["Bad Debt Expense"] = []
    
    def addCash(self, amount):
        self.assets["Cash"].append(amount)
    
    def addPrepaid(self, amount):
        cash_change = Cash(-(amount.value), amount.date)
        self.assets["Prepaid Expense"].append(amount)
        self.assets["Cash"].append(cash_change)
    
    def addAccountsReceivable(self, amount):
        self.assets["Accounts Receivable"].append(amount)
    
    def changeAccountsReceivable(self, amount, date):
        is_doubtful = input("0 to Cash, 1 to Allowance for Doubtful Accounts, and 2 to Bad Debt Expense: ")
        if(is_doubtful == '0'):
            cash_change = Cash(amount, date)
            self.assets["Cash"].append(cash_change)
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
        elif(is_doubtful == '1'):
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
            DA_change = allowance_for_doubtful_accounts(amount, date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
        else:
            AR_change = accountsReceivable(-(amount), date, True)
            self.assets["Accounts Receivable"].append(AR_change)
            BDR_change = badDebtExpense(amount, date)
            self.assets["Bad Debt Expense"].append(BDR_change)
    
    def changeAllowanceForDoubtfulAccount(self, amount, date):
        is_doubtful = input("0 to Cash, and 1 to Bad Debt Expense: ")
        if(is_doubtful == '0'):
            cash_change = Cash(amount, date)
            self.assets["Cash"].append(cash_change)
            DA_change = allowance_for_doubtful_accounts(-(amount), date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
        else:
            DA_change = allowance_for_doubtful_accounts(-(amount), date)
            self.assets["Allowance for Doubtful Accounts"].append(DA_change)
            BDR_change = badDebtExpense(amount, date)
            self.assets["Bad Debt Expense"].append(BDR_change)
            

    def showAllAssets(self):
        for i in self.assets.keys():
            retval = 0
            toPrint = self.assets[i]
            print("Asset ", i,": ")
            for j in range(len(toPrint)):
                retval += toPrint[j].getValue()
                print(toPrint[j].date, " ", toPrint[j].getValue())
            print("total amount ", retval)