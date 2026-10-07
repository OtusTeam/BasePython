class AppError(Exception):
    pass


class UserError(AppError):
    pass


class UserAlreadyExistsError(UserError):
    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__(username)


class AuthError(AppError):
    pass


class InvalidUsernameOrPassword(AuthError):
    pass
