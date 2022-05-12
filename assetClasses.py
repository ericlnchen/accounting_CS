
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

class prepaidExpense(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)
    
class Cash(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)

class accountsReceivable(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)

class inventory(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)

class PPE(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, False)

class investment(Asset):
    def __init__(self, value, date, isCurrent):
        super().__init__(value, date, isCurrent)

class purchases(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)

class accumulatedDepreciation(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)

class allowance_for_doubtful_accounts(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)

class badDebtExpense(Asset):
    def __init__(self, value, date):
        super().__init__(value, date, True)