"""
DB helper module
"""

def get_rates(currency, dttm):
    return {'12:00:01': 30.5,
            '14:00:05': 31.7}


def save_rate(currency, rate):
    print(f'saved to db: {currency} ({rate})')


if __name__ == '__main__':
    save_rate('EUR', 39)
