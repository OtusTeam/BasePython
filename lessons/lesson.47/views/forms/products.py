from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import (
    DataRequired,
    NumberRange,
    ValidationError,
)

from views.products.crud import products_storage


def validate_product_name(form, field):
    product_name = field.data
    # TODO: update: check same id
    if request.method == "POST" and products_storage.name_exists(product_name):
        raise ValidationError(
            f"Product with name {product_name!r} already exists!",
        )


class ProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        validators=[
            DataRequired(),
            validate_product_name,
        ],
    )
    price = IntegerField(
        label="Price",
        validators=[NumberRange(min=1)],
    )

    add = SubmitField(
        label="Create",
    )
