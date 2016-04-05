class DifferentCurrencyCodeError(Exception):
    pass

class UnknownCurrencyCodeError(Exception):
    pass

class Currency:

    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    # def __init__(self, amount, currency_code, currency_symbol=None,):
    #     self.amount = amount
    #     self.currency_code = currency_code
    #     currency_symbol = {
    #     '$': 'USD',
    #     '﹩': 'USD',
    #     '＄': 'USD',
    #     '€': 'EUR',
    #     '¥': 'YEN',
    #     '￥': 'YEN',
    #     '£': 'GBP',
    #     '￡' 'GBP',
    #     '₹': 'INR',
    #     '₱': 'MXN'
    #     }


    def __str__(self):
        return str(self.amount) + ' ' + self.currency_code

    def __eq__(self, other):
        # if self.amount == other.amount:
            # if self.currency_code == other.currency_code:
            #     return True
            # else:
            #     return False
        return self.amount == other.amount and self.currency_code = other.currency_code

    def __ne__(self, other):
        if self.amount != other.amount:
            return True
        elif self.currency_code != other.currency_code:
            return True
        else:
            return False
        # return self.amount != other.amount or self.currency_code != other.currency_code

    def __add__(self, other):
        if __eq__(self, other) == True:
            return self.amount + other.amount
        else:
            raise DifferentCurrencyCodeError

    def __sub__(self, other):
        if __eq__(self, other) == True:
            return self.amount - other.amount
        else:
            raise DifferentCurrencyCodeError

    def __mul__(self, multiplier):
        try:
            return round(self.value, 2) += self.value * float(multipier)
        except:
            return "You can only multiply by a float or integer."
