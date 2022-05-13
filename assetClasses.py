
# An asset is an item of value that a business owns.
# It can be current or non-current based on whether or not the company
# expects it to be used and sold in the following calendar year.
# All assets are debited when they increase, and credit when they decrease.
# Assets equal liability plus owners' equity.

class Asset(object):
    def __init__(self, value, date, isCurrent):
        self.value = value
        self.date = date
        self.isCurrent = isCurrent

    def getValue(self):
        return self.value

    def getDate(self):
        return self.date

    def getIsCurrent(self):
        return self.isCurrent


# Prepaid expenses are future expenses paid in advance.
# They are first recorded as current assets, but are later recorded as an expense
# when the asset is realized (used up) over time.
class prepaidExpense(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)


# Cash is money that is readily available for use.
class Cash(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)


# Accounts receivable are funds that customers owe the company for goods and services
# that have been invoiced (in other would what you expect to receive).
# It is credited/decreased when:
# (1) Cash is received
# (2) Allowance for doubtful accounts increases
# (3) Bad debt expense is recognized
class accountsReceivable(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)


# Inventory counts the value of the stock of the company (i.e. raw materials, WIP, finished goods).
class inventory(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)


# PPE is the property, plant, and equipment a company owns.
# It is in most cases considered a long-term/non-current asset.
class PPE(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, False)


# Investment assets are tangible or intangible items obtained with the intent of it generating additional
# income or held for speculative purposes (e.g. mutual funds, stocks, bonds, real estate).
class investment(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)


# Accumulated depreciation is the total amount of depreciation that has been
# expensed against the value of assets over its useful life.
# It is a contra-asset, meaning its natural balance is a credit (i.e. credited when it increases).
# Depreciation expense is debited whenever Accumulated depreciation is credited.
class accumulatedDepreciation(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)


# Allowance for doubtful accounts represents the best estimate of the amount of accounts receivable.
# that will not be paid by customers.
# Accounts receivable is credited/decreased whenever Allowance for doubtful accounts is debited/increased.
class allowance_for_doubtful_accounts(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)


# Bad debt expense represents Accounts receivables that are no longer collectible.
# It is debited/increased either when:
# (1) Accounts receivable is credited/decreased
# (2) Allowance for doubtful accounts is credited/decreased
class badDebtExpense(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)