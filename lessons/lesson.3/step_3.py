products = ['phone', '', 'tablet', 'notebook', 'watch', 'tablet']
# products = ['phone', 'tablet', 'notebook', 'watch']

products_f = []  # memory O(n)
for item in products:
    if item and item not in products_f:
        products_f.append(item)
print(products_f)

# products_f = [item for item in products if item]

products_f = [item
              for item in products
              if item]  # O(n)

print(products_f)
