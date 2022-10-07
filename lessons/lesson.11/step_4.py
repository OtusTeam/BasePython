with open('otus_2.html', 'r', encoding='utf-8') as f:
    # f_iter = iter(f)
    # print(next(f_iter).strip(), end='')
    # print(next(f_iter).strip(), end='')
    # print(next(f_iter).strip(), end='')
    for row in f:
        print(row.strip())
