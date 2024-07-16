# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .error_detail import ErrorDetail


class Error(pydantic_v1.BaseModel):
    sub_category: typing.Optional[str] = pydantic_v1.Field(alias="subCategory", default=None)
    """
    A specific category that contains more specific detail about the error
    """

    context: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic_v1.Field(default=None)
    """
    Context about the error condition
    """

    correlation_id: str = pydantic_v1.Field(alias="correlationId")
    """
    A unique identifier for the request. Include this value with any error reports or support tickets
    """

    links: typing.Optional[typing.Dict[str, str]] = pydantic_v1.Field(default=None)
    """
    A map of link names to associated URIs containing documentation about the error or recommended remediation steps
    """

    message: str = pydantic_v1.Field()
    """
    A human readable message describing the error along with remediation steps where appropriate
    """

    category: str = pydantic_v1.Field()
    """
    The error category
    """

    errors: typing.Optional[typing.List[ErrorDetail]] = pydantic_v1.Field(default=None)
    """
    further information about the error
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
