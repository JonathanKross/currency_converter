sample_conversion: {
    'USD': 1.0,
    'EUR': 0.87,
    'GBP': 0.70,
    'INR': 66.10,
    'AUD': 1.31
}


class Currency_Converter:

    def __init__(self, currency_code_dict):
        self.currency_codes = currency_code_dict

    def convert(self, currency, currency_code):
        pass





class DifferentCurrencyCodeError(Exception):
    pass

if currency_a != currency_b:
    raise CustomCurrencyCodeError
