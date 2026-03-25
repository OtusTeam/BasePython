file_object = open('data/info_append.txt', 'a')
file_object.write('Hello World123\n')
file_object.write('Hello World456\n')
file_object.write('Hello World789\n')
file_object.write(str(12345)+'\n')
file_object.close()


file_object = open('data/empty.txt', 'a')
file_object.close()


lines_str = ['123\n', '456\n', 'Hello world\n', 'Python\n']
file_object = open('data/info_lines_append.txt', 'a')
file_object.writelines(lines_str)
file_object.close()


