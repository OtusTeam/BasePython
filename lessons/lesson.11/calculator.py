class ExpressionCalculator:
    def __init__(self):
        self.operators = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def calculate(self, expression: str) -> float:
        tokens = self.tokenize(expression)
        if not tokens:
            raise ValueError("Некорректное выражение")
        postfix = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix)

    def tokenize(self, expression: str):
        """
        Преобразует строку выражения в список токенов (чисел и операторов).

        Args:
            expression (str): Математическое выражение в виде строки.

        Returns:
            list: Список токенов (чисел и операторов).
        """
        tokens = []  # Список для хранения токенов (чисел и операторов)
        num = ""  # Строка для накопления цифр числа
        for char in expression:
            if char.isdigit() or char == ".":  # Если символ - цифра или точка
                num += char  # Добавляем его к текущему числу
            else:
                if num:  # Если число накопилось
                    tokens.append(
                        float(num)
                    )  # Преобразуем его в float и добавляем в токены
                    num = ""  # Сбрасываем накопитель чисел
                if (
                    char in self.operators or char in "()"
                ):  # Если символ - оператор или скобка
                    tokens.append(char)  # Добавляем его в токены
        if num:  # Если после цикла осталось накопленное число
            tokens.append(float(num))  # Преобразуем его в float и добавляем в токены
        return tokens  # Возвращаем список токенов

    def infix_to_postfix(self, tokens):
        """
        Преобразует инфиксное выражение (обычная форма записи) в постфиксное
        (обратная польская нотация).

        Args:
            tokens (list): Список токенов (чисел и операторов) инфиксного выражения.

        Returns:
            list: Список токенов в постфиксной нотации.
        """
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Определяем приоритет операторов
        output = []  # Список для хранения постфиксного выражения
        stack = []  # Стек для операторов и скобок
        for token in tokens:
            if isinstance(token, float):  # Если токен - число
                output.append(token)  # Добавляем его в выходной список
            elif token in self.operators:  # Если токен - оператор
                while (
                    stack
                    and stack[-1] != "("
                    and precedence[stack[-1]] >= precedence[token]
                ):
                    output.append(
                        stack.pop()
                    )  # Перемещаем оператор из стека в выходной список
                stack.append(token)  # Добавляем текущий оператор в стек
            elif token == "(":  # Если токен - открывающая скобка
                stack.append(token)  # Добавляем ее в стек
            elif token == ")":  # Если токен - закрывающая скобка
                while stack and stack[-1] != "(":  # Пока не встретим открывающую скобку
                    output.append(
                        stack.pop()
                    )  # Перемещаем операторы из стека в выходной список
                stack.pop()  # Удаляем открывающую скобку из стека
        while stack:  # Перемещаем оставшиеся операторы из стека в выходной список
            output.append(stack.pop())
        return output  # Возвращаем постфиксное выражение

    def evaluate_postfix(self, tokens):
        """
        Вычисляет значение постфиксного выражения.
        """
        stack = []  # Стек для хранения чисел
        for token in tokens:
            if isinstance(token, float):  # Если токен - число
                stack.append(token)  # Добавляем его в стек
            elif token in self.operators:  # Если токен - оператор
                if (
                    len(stack) < 2
                ):  # Проверяем, что в стеке достаточно чисел для операции
                    raise ValueError(
                        "Invalid expression"
                    )  # Если нет, выбрасываем исключение
                b = stack.pop()  # Извлекаем два числа из стека
                a = stack.pop()
                stack.append(
                    self.operators[token](a, b)
                )  # Выполняем операцию и результат добавляем в стек
        if len(stack) != 1:  # В конце в стеке должно остаться одно число - результат
            raise ValueError("Invalid expression")  # Если нет, выбрасываем исключение
        return stack[0]  # Возвращаем результат


if __name__ == "__main__":
    calculator = ExpressionCalculator()
    exp = "(2 + 3) * (4 - 2)"
    print(exp)
    tokenize = calculator.tokenize(exp)
    print(f"{tokenize=}")
    infix = calculator.infix_to_postfix(tokenize)
    print(f"infix_to_postfix = {infix}")
    res = calculator.evaluate_postfix(infix)
    print(f"res={res}")
