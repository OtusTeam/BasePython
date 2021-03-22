class Basket:

    def __init__(self):
        self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, percentage):
        # if percentage < 0:
        #     raise PriceValueError()
        try:
            self._discount = float(percentage)
        except Exception as ex:
            print(ex)
            raise PriceValueError(percentage)


# заглушка дает понять более точно, в чем проблема
class PriceValueError(Exception):
    pass


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
