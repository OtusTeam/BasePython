import re


pattern = 'cat'
string = 'dog and cat'
result = re.match(pattern, string)

print(type(result))
print(result)


pattern1 = 'cat'
string1 = 'cat and dog'
result1 = re.match(pattern1, string1)

if result1:
    print(result1)
    print(result1.group())
    # print(type(result1))


pattern2 = 'cat'
string2 = 'dog and cat'
result2 = re.search(pattern2, string2)
if result2:
    print(result2)
    print(result2.group())
    # print(type(result2))


pattern2 = 'cat'
string2 = 'dog and cat cat cat'
result3 = re.findall(pattern2, string2)
print(result3)
print(type(result3))


pattern2 = r'a[xyz]c'
string2 = 'Мaоcй aaxcномcер 1a23c c 46-78978978, код 137'
result3 = re.findall(pattern2, string2)
print(result3)
print(type(result3))


