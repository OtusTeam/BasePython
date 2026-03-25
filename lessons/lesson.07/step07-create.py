file_object = open('data/info.txt', 'w')
file_object.write('Hello World123\n')
file_object.write('Hello World456\n')
file_object.write('Hello World789\n')
file_object.close()


file_object = open('data/empty.txt', 'w')
file_object.close()


lines_str = ['123\n', '456\n', 'Hello world\n', 'Python\n']
file_object = open('data/info_lines.txt', 'w')
file_object.writelines(lines_str)
file_object.close()


