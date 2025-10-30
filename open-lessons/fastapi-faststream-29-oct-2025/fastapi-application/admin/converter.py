from typing import Any

from sqladmin.forms import (
    ModelConverter as ModelConverterGeneric,
    converts,
)
from sqlalchemy.orm import ColumnProperty
from sqladmin.fields import (
    DateTimeField,
)


class ModelConverter(ModelConverterGeneric):

    @converts("TIMESTAMPAware")
    def conv_timestamp_aware(
        self,
        model: type,
        prop: ColumnProperty,
        kwargs: dict[str, Any],
    ):
        return DateTimeField(**kwargs)
