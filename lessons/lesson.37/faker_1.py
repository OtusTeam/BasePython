import faker

faker.Faker.seed("zoo-tests")

# faker_inst = faker.Faker()
faker_inst = faker.Faker('ru_RU')
# faker_inst = faker.Faker('es_ES')

# print(faker_inst.name(), type(faker_inst.name()))
# print(faker_inst.address())
# print(faker_inst.address())

# sentence = faker_inst.sentence()
sentence = faker_inst.sentence(ext_word_list=["типизация", "компилятор", "выполнить"])
print(sentence)
