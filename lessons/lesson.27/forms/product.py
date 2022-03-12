from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField("Product name", name="product-name", validators=[
        DataRequired(),
        Length(min=3),
    ])
    is_new = BooleanField("Is new", default=False)
