with open('otus_2.html', 'r', encoding='utf-8') as f:
    content = f.read().splitlines()
    # content = []
    # for row in f:
    #     content.append(row)

print(*content, sep='\n')
