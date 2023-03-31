from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        render_kw={"placeholder": "Desktop"},
    )
    short_description = StringField(
        "Short description",
        validators=[DataRequired()],
    )
