from decimal import Decimal


def get_currency_rate(currency='USD'):
    return {'10:00': Decimal(1.5),
            '11:00': Decimal(1.45)}
