# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class PageIncrementAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PageIncrementAllOf - a model defined in OpenAPI

        page_size: The page_size of this PageIncrementAllOf.
        start_from_page: The start_from_page of this PageIncrementAllOf [Optional].
    """

    page_size: int = Field(alias="page_size")
    start_from_page: Optional[int] = Field(alias="start_from_page", default=None)

PageIncrementAllOf.update_forward_refs()