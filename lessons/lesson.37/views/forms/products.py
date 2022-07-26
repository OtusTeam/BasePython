from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    """
    Product Form
    """
    name = StringField(
        label="Product Name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ]
    )
