class ApplicationError(Exception):
    code = "application_error"
    message = "Application error"


class NotFoundError(ApplicationError):
    pass


class ConflictError(ApplicationError):
    pass


class TemporaryUnavailableError(ApplicationError):
    pass


class AuthorNotFoundError(NotFoundError):
    code = "author_not_found"

    def __init__(self, author_id: int) -> None:
        self.message = f"Author {author_id} not found"
        super().__init__(self.message)


class AuthorAlreadyExistsError(ConflictError):
    code = "author_already_exists"

    def __init__(self, name: str) -> None:
        self.message = f"Author {name!r} already exists"
        super().__init__(self.message)


class BookNotFoundError(NotFoundError):
    code = "book_not_found"

    def __init__(self, book_id: int) -> None:
        self.message = f"Book {book_id} not found"
        super().__init__(self.message)


class DataConflictError(ConflictError):
    code = "data_conflict"
    message = "Operation violates a database constraint"


class DatabaseBusyError(TemporaryUnavailableError):
    code = "database_busy"
    message = "No database connection is currently available"


class DatabaseUnavailableError(TemporaryUnavailableError):
    code = "database_unavailable"
    message = "Database is temporarily unavailable"
