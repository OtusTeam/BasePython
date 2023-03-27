# from helpers import BASE_CURRENCY
BASE_CURRENCY = 'RUB'


def get_currency_rate(currency=BASE_CURRENCY):
    return {'10:00': 1.5,
            '11:00': 1.45}


def save_currency_rate(currency, rate):
    return 'saved'


if __name__ == '__main__':
    print(__name__, 'get_currency_rate', get_currency_rate())
