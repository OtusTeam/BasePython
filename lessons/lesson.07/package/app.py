
from corepackage.baskets import Basket, PriceValueError
# from corepackage import Basket, PriceValueError

print(__name__)

if __name__ == '__main__':
    try:
        basket = Basket()
        basket.discount = 'hello'
    except (PriceValueError, AttributeError) as e:
        print(e)
        print(f'Exception is raised for value: {e.args[0]}')
    except Exception as e:
        print(f'Exception is raised: {e.args}')
    else:
        print('commit')
    finally:
        print('close connection')
