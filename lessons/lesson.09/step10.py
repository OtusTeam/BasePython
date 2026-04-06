class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.tasks):
            raise StopIteration

        current = self.tasks[self.index]
        self.index += 1
        return current


task_list = ['Почитать', 'Посмотреть', 'Погулять', 'Поспать']

tasks = TaskList(task_list)

# for task in tasks:
#     print(task)

my_iter = iter(tasks)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))