from typing import ClassVar

from beets import dbcore
from beets.dbcore import query, sort
from beets.dbcore.db import FormattedMapping, Index
from beets.library import LibModel
from beets.util import cached_classproperty


class SortFixture(sort.FieldSort):
    pass


class QueryFixture(query.FieldQuery):
    def __init__(self, pattern):
        self.pattern = pattern

    def clause(self):
        return None, ()

    def match(self):
        return True


class ModelFixture1(LibModel):
    _table = "test"
    _flex_table = "testflex"
    _fields: ClassVar[dict[str, dbcore.types.Type]] = {
        "id": dbcore.types.PRIMARY_ID,
        "field_one": dbcore.types.INTEGER,
        "field_two": dbcore.types.STRING,
        "path": dbcore.types.PathType(),
    }

    _sorts: ClassVar[dict[str, type[sort.FieldSort]]] = {
        "some_sort": SortFixture
    }
    _indices = (Index("field_one_index", ("field_one",)),)
    _formatter = FormattedMapping
    _search_fields = ("artist", "title")

    @cached_classproperty
    def _types(cls):
        return {"some_float_field": dbcore.types.FLOAT}

    @cached_classproperty
    def _queries(cls):
        return {"some_query": QueryFixture, "year": dbcore.query.NumericQuery}

    @classmethod
    def _getters(cls):
        return {}

    def _template_funcs(self):
        return {}
