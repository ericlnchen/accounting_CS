from assetClasses import *
from liabilityClasses import *
from accounts import *

if __name__ == '__main__':

    quener = Account()
    c1 = Cash(500, "05/11/2022")
    ar1 = accountsReceivable(30000, "05/11/2022", True)
    quener.addCash(c1)
    quener.addAccountsReceivable(ar1)
    quener.changeAccountsReceivable(1000, "05/12/2022")
    quener.changeAccountsReceivable(250, "05/25/2022")
    quener.changeAllowanceForDoubtfulAccount(333, "05/26/2022")
    quener.changeAllowanceForDoubtfulAccount(125, "05/29/2022")
    quener.showAllAssets()
    print("got here")

