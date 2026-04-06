class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        return f'Сумма: {self.rub} руб. {self.kop} коп.'

    def __call__(self, count=10):
        return f'У нас есть денег: {self.rub * count} руб. {self.kop * count} коп.'


m_1 = Money(500, 70)
print(m_1)

m_2 = Money(200, 50)
print(m_2)

# m_1.__call__()
print(m_1(100))