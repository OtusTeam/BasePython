import re 

text = '''
Customer report:  
Name: John Doe  
Email: john.doe1990@example.com  
Phone: +7-912-555-12-34  
Date of purchase: 2025-02-24  
Amount: $125.50  
IP: 192.168.1.10

---

Name: Alice Smith  
Email: alice.smith@company.org
Phone: +7-495-123-45-67  
Date of purchase: 2025-03-21  
Amount: $89.99  
IP: 10.0.0.5

---

Name: Bob Stone  
Email: bob.stone123@gmail.com  
Phone: +7-911-000-00-00  
Date of purchase: 2025-03-15  
Amount: $230.00  
IP: 172.16.0.1
'''

# Поиск первого совпадения
match_text = re.search(r'([\w\.\-]+)@([\w\.]+)\.(\w+\s)', text)

if match_text:
    address = match_text.group(1)
    domen = match_text.group(2)
    suffix = match_text.group(3)
    print(f'{address=}\n{domen=}\n{suffix=}')

# Поиск всех совпадений
all_matches = re.findall(r'[\w\.\-]+@[\w\.]+\.\w+\s', text)

if match_text:
    print(all_matches)

# Замена и очистка текста
text = "John   Doe  !!!"
cleaned = re.sub(r'\s+', ' ', text)
cleaned = re.sub(r'[!]+', '', cleaned)
cleaned = re.sub(r'\s+$', '', cleaned)
print(f'{cleaned=}')