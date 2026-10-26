"""
Arrange - подготовка
  # быстрая (короткая) подготовка окружения для теста

Act - действие
  # выполняем то (что-то одно), что тестируем

Assert - проверка
  # убеждаемся, что результаты совпадают с ожидаемыми

"""

import json
from dataclasses import dataclass

import pytest

from homework.config import CONTACTS_FILE_NAME
from homework.new_contact import new_reg
from homework import new_contact

# pytestmark = pytest.mark.regs


@pytest.fixture
def clear_contacts_file(mocker, tmp_path):
    contacts_file = tmp_path / CONTACTS_FILE_NAME
    mocker.patch.object(new_contact, "CONTACTS_FILE_NAME", contacts_file)
    return contacts_file


@dataclass(frozen=True, slots=True)
class InputParams:
    name: str
    phone: str
    comment: str


@pytest.fixture
def user_input(request, mocker):
    # аннотация только для меня!!
    # код её игнорирует
    input_params: InputParams = request.param
    if isinstance(input_params, InputParams):
        inputs = [
            input_params.name,
            input_params.phone,
            input_params.comment,
        ]
    else:
        inputs = input_params
    mocker.patch(
        "homework.new_contact.input",
        return_value="123",
        side_effect=inputs,
    )
    return input_params


# перемножаем просто для примера
@pytest.mark.parametrize(
    "name",
    [
        pytest.param("Alice", id="Alice"),
        pytest.param("Alice'n'Bob", id="with-ticks"),
    ],
)
@pytest.mark.parametrize(
    "comment",
    [
        pytest.param("hello world", id="with-space"),
        pytest.param("[comment]", id="with-brackets"),
    ],
)
def test_new_reg(name, comment, mocker, clear_contacts_file):
    # Arrange

    # name = "Alice"
    phone = "89101235566"
    # comment = "Bob's friend"
    mocker.patch(
        "homework.new_contact.input",
        return_value="123",
        side_effect=[
            name,
            phone,
            comment,
        ],
    )

    # Act
    new_reg()

    # Assert

    assert clear_contacts_file.exists(), "file should exist after adding"
    with clear_contacts_file.open() as f:
        saved_contact = json.loads(f.readline())
    assert saved_contact == {
        "name": name,
        "phone": int(phone),
        "comment": comment,
    }, "values should be same, phone should integer"


# Arrange
@pytest.mark.parametrize(
    "user_input",
    [
        pytest.param(
            [
                "Alice",
                "foo-bar",
                "123456",
                "Bob's friend",
            ],
            id="non-int-phone",
        ),
    ],
    indirect=["user_input"],
)
# @pytest.mark.corner_cases
def test_new_reg_says_error_for_non_int(
    user_input,
    clear_contacts_file,
    capsys,
):
    # Act
    new_reg()

    # Assert
    outs = capsys.readouterr()
    assert "Введите только цифры" in outs.out
