class DifferentCurrencyCodeError(Exception):
    pass

class UnknownCurrencySymbolError(Exception):
    pass

class Currency:
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code
        currency_symbol_dict = {
        '$': 'USD',
        '﹩': 'USD',
        '＄': 'USD',
        '€': 'EUR',
        '¥': 'YEN',
        '￥': 'YEN',
        '£': 'GBP',
        '￡': 'GBP',
        '₹': 'INR',
        '₱': 'MXN',
        }
        if currency_symbol:
            for symbol in currency_symbol:
                if '$' or '﹩' or '＄' in currency_symbol[0]:
                    self.currency_code = 'USD'
                    self.amount = float(currency_symbol[1:])
                elif '€' in currency_symbol[0]:
                    self.currency_code = 'EUR'
                    self.amount = float(currency_symbol[1:])
                elif '¥' or '￥' in currency_symbol[0]:
                    self.currency_code = 'YEN'
                    self.amount = float(currency_symbol[1:])
                elif '£' or '￡' in currency_symbol[0]:
                    self.currency_code = 'GBP'
                    self.amount = float(currency_symbol[1:])
                elif '₹' in currency_symbol[0]:
                    self.currency_code = 'INR'
                    self.amount = float(currency_symbol[1:])
                elif '₱' in currency_symbol[0]:
                    self.currency_code = 'MXN'
                    self.amount = float(currency_symbol[1:])
                else:
                    raise UnknownCurrencySymbolError


    def __str__(self):
        return str(self.amount) + ' ' + self.currency_code

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def __ne__(self, other):
        if self.amount != other.amount:
            return True
        elif self.currency_code != other.currency_code:
            return True
        else:
            return False

    def __add__(self, other):
        try:
            if self.currency_code == other.currency_code:
                return Currency(self.amount + other.amount, self.currency_code)
        except:
            raise DifferentCurrencyCodeError()

    def __sub__(self, other):
        try:
            if self.currency_code == other.currency_code:
                return Currency(self.amount - other.amount, self.currency_code)
        except:
            raise DifferentCurrencyCodeError()

    def __mul__(self, multiplier):
        try:
            return Currency(round(self.amount * multiplier), 2), self.currency_code)
        except:
            return "You can only multiply by a float or integer."

# if __name__ == '__main__':
#     main()
