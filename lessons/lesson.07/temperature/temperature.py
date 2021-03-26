class Test:
    def __init__(self):
        self._temperature = 0.0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @temperature.getter
    def temperature(self):
        print(f"my temperature is {self._temperature}")


t0 = Test()  # default value
print(t0.temperature)
# t0.temperature = 666.7  # assign a new value through =
# t0.temperature  # get value through obj call
