import os

# print(os.name)
# print(os.environ)

# otus_admin_user = 'Otus'
otus_admin_user = os.environ.get('OTUS_ADMIN_USER', 'Otus')
print(otus_admin_user)

