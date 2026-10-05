class EmailStore:
    def __init__(self):
        self._known_emails = set[str]()

    def add(self, email: str) -> None:
        self._known_emails.add(email)

    def remove(self, email: str) -> None:
        self._known_emails.discard(email)

    def exists(self, email: str) -> bool:
        return email in self._known_emails


email_store = EmailStore()


class Student:
    def __init__(self, name: str, email: str | None) -> None:
        self.name = name
        if email_store.exists(email):
            email = None
        else:
            email_store.add(email)
        self.email = email

    def change_email(self, new_email: str) -> bool:
        """
        :param new_email:
        :return: True если получилось сменить и False если нет.
        """
        print("Change email for", self.name, "from", self.email, "to", new_email)
        if email_store.exists(new_email):
            print("email", new_email, "already exists")
            return False

        email_store.remove(self.email)
        self.email = new_email
        email_store.add(new_email)
        return True


bob = Student("Bob", "bob@example.com")
print("name:", bob.name)
print("bob's email:", bob.email)
bob.change_email("example@ya.ru")
print("bob's email:", bob.email)


john = Student("John", "john@example.com")
print("name:", john.name)
print("john's email:", john.email)
john.change_email("example@ya.ru")
print("john's email:", john.email)


# print(Student)
# print(Student.mro())
#
# student = Student()
# print(type(student))
# student.name = "Bob"
# print("name:", student.name)
#
# john = Student()
# print("name:", john.name)

print(email_store._known_emails)
email_store._known_emails.add("foo.bar")
print(email_store._known_emails)
