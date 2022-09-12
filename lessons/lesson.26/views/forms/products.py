from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class CreateProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ],
    )
    is_new = BooleanField(
        label="Is new product?",
        default=False,
    )
