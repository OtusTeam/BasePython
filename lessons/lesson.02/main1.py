x = 1
my_str = """Pyth"on"""
my_str_1 = '''Java'''
y = 3

format_str = f'У нас {x + 10} {my_str} А также  {y * 10} {my_str_1}'

print(x, my_str, y, my_str_1, sep='', end='---------')
print(x, my_str, y, my_str_1,  sep='--', end='\n\n')
print('У нас', x * 10, my_str, 'А также ', y + 10, my_str_1)
print(format_str)