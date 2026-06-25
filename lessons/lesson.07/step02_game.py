from typing import Callable


def guess_number(num: int, count: int) -> Callable[[], None]:
    def func_game():
        for i in range(1, count + 1):
            print(f'Попытка № {i}')
            answer = int(input('Введите число: '))
            if answer == num:
                print("Угадал")
                break
            elif answer > num:
                print("Твоё число больше")
            elif answer < num:
                print("Твоё число меньше")
        else:
            print(f'Попытки закончились. Загаднное число {num}')
    return func_game


if __name__ == '__main__':
    game = guess_number(17, 5)
    game()
