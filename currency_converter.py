sample_conversion: {
    'USD': 1.0,
    'EUR': 0.87,
    'GBP': 0.70,
    'INR': 66.10,
    'AUD': 1.31
}

class UnknownCurrencyCodeError(Exception):
    pass

class Currency_Converter:

    def __init__(self, currency_code_dict):
        self.currency_code_dict = currency_code_dict

    def convert(self, currency, currency_code):
        if currency.currency_code in self.currency_code_dict.key() and currency_code in self.currency_code_dict.key():
            if currency.currency_code == currency_code:
                return Currency(currency.amount, currency_code)
            else:
                return Currency(currency.amount * self.currency_code_dict[currency_code] / self.currency_code_dict[currency.currency_code], currency_code)
        else:
            raise UnknownCurrencyCodeError("Don't know one of those currencies.")

    def

    def convert(self, from_currency, to_code):
        if from_currency.code == to_code:
            return from_currency
        elif (to_code not in self.exchange_rate or
            from_currency.code not in self.exchange_rate):
            raise UnknownCurrencyCodeError()
        else:
            return Currency(to_code, from_currency.value * self.exchange_rate[to_code] / self.exchange_rate)



if currency_a != currency_b:
    raise CustomCurrencyCodeError
