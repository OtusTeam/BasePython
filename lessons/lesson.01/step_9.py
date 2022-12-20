age = 25

# yaml
if age >= 18:
    print('access granted')
elif age > 21:  # bug
    print('full acces')
    if age > 45:
        print(')')
else:
    print('forbidden')
