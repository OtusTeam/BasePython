with open('otus_2.html', 'r', encoding='utf-8') as f:
    # content = [el.strip() for el in f.readlines()]
    content = f.read().splitlines()
    # content = f.read(10)
    # content = ''
    # for row in f:
    #     content += row

print(content)
