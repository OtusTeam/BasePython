class EmailStore:
    def __init__(self):
        self._known_emails = set[str]()

    def add(self, email: str) -> None:
        self._known_emails.add(email)

    def remove(self, email: str) -> None:
        self._known_emails.discard(email)

    def exists(self, email: str) -> bool:
        return email in self._known_emails

    def __iter__(self):
        return iter(self._known_emails)


email_store = EmailStore()
email_store.add("foo")
email_store.add("bar")
email_store.add("fizz")
email_store.add("buzz")

for email_addr in email_store:
    print(email_addr)
