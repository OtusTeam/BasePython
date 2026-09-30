student_name = "Bob"
student_email = "bob@example.com"


def send_welcome_email(
    name: str,
    email: str,
) -> None:
    text = f"Hi, {name}! Welcome."
    send_email(
        from_admin,
        subject="Welcome",
        to=[email],
        text=text,
    )


def update_student_email(
    name: str,
    old_email: str,
    new_email: str,
) -> tuple[str, str]:
    send_email_updated_email(...)
    return name, new_email


student = {
    "name": "Bob",
    "email": "bob@example.com",
}
# student.update(...)
# student.pop("name")
# student.pop("email")
