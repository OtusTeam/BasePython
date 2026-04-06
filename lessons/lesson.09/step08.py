class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        return f'Сумма: {self.rub} руб. {self.kop} коп.'

    # obj1 + obj2
    def __add__(self, other):
        # if isinstance(other, Money):
        all_kop = self.kop + other.kop
        new_rub = self.rub + other.rub + (all_kop // 100 )
        new_kop = all_kop % 100

        return Money(new_rub, new_kop)

    # obj += 1
    def __radd__(self, values):
        # if isinstance(other, Money):
        self.kop = self.kop + values
        self.rub = self.rub + values

        # return (new_rub, new_kop)

    def __sub__(self, other):
        new_rub = self.rub - other.rub
        new_kop = self.kop - other.kop

        return Money(new_rub, new_kop)

    def __mul__(self, other):
        new_rub = self.rub * other
        new_kop = self.kop * other

        return Money(new_rub, new_kop)




m_1 = Money(500, 70)
print(m_1)

m_2 = Money(200, 50)
print(m_2)

m3 = m_1 + m_2
print(m3)

# __sub__
m_4 = m_1 - m_2
print(m_4)

# __mul__
m_5 = m_1 * 10
print(m_5)