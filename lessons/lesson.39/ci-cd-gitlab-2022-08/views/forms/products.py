from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        # render_kw={'class': 'form-control'}
    )
    description = TextAreaField(validators=[DataRequired()])
