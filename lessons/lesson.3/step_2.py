# products = ['phone', '', 'tablet', 'notebook', 'watch']
products = ['phone', 'tablet', 'notebook', 'watch']

msg = 'error occurred'
for item in products:
    if not item:
        break
    print(item)
else:
    msg = 'ok'
print(msg)


