# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""DBCore is an abstract database package that forms the basis for beets'
Library.
"""

from beets.util.deprecation import deprecate_for_maintainers, deprecate_imports

from .db import Database, Index, Model, Results
from .query import (
    AndQuery,
    FieldQuery,
    InvalidQueryError,
    MatchQuery,
    OrQuery,
    Query,
)
from .queryparse import ModelQuery
from .types import Type

_NEW_METHOD_BY_OLD_METHOD_NAME = {
    "query_from_strings": ModelQuery.build_and_query,
    "sort_from_strings": ModelQuery.get_sort,
    "parse_sorted_query": ModelQuery.parse,
}


def __getattr__(name: str):
    for old_method_name, new_method in _NEW_METHOD_BY_OLD_METHOD_NAME.items():
        if name == old_method_name:
            deprecate_for_maintainers(
                f"'beets.dbcore.{name}'",
                f"'beets.dbcore.{new_method.__qualname__}'",
            )
            return new_method

    return deprecate_imports(__name__, {}, name)


__all__ = [
    "AndQuery",
    "Database",
    "FieldQuery",
    "Index",
    "InvalidQueryError",
    "MatchQuery",
    "Model",
    "ModelQuery",
    "OrQuery",
    "Query",
    "Results",
    "Type",
]
