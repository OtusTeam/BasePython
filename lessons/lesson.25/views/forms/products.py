from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        label="Product Name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ]
    )
    is_new = BooleanField(
        label="Is new product",
        name="is-new",
        default=False,
    )
