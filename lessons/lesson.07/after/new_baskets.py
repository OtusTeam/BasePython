class Basket:

    def __init__(self, current_size=0):
        self.current_size = current_size

    def __str__(self):
        return f"{self.__class__.__name__} : current_size = {self.current_size}"
