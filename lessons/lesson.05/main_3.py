def greet(lang='python'):
    print('Как тебя зовут?')
    name = input()
    print(f'Привет {name}, Твой язык - {lang}!!!')


name = 'Ivan'
lang2 = 'c++'
greet()
print(name)
print(lang2)

name = 'Ivan1'
lang = 'Java'
greet()
print(name)

name = 'Ivan2'
lang1 = 'python'
greet(lang1)
print(name)