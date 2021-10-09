salary = [159.3, 563.7, 578.1, 248.3]

scale = 1.05
# salary_upd = [round(el * scale, 2) for el in salary]
salary_upd = [el * scale for el in salary]
# salary_upd_rounded = map(round, salary_upd)
salary_upd_rounded = list(map(lambda x: round(x, 2), salary_upd))
# salary_upd = salary * scale
print(salary)
print(salary_upd)
print(salary_upd_rounded)
