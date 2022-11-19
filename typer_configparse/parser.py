from enum import Flag, auto
from io import TextIOBase
from typing import Optional, Type, Union

import toml
import yaml
from pydantic import BaseModel


class ConfigMergeType(Flag):
    """Defines how to merge values from multiple config files.

    When USE_FIRST_FILE is set, all other flags are ignored, and only the first matching file will be used for all
        values.
    When DEEP_MERGE is set, nested dicts are merged together with leaf override behavior described by
        USE_LAST_DEFINITION.  When set with LIST_MERGE, lists of dicts are merged by index.

        When unset, only the top-level names are merged, with their values completely overridden by the new value as
        described by USE_LAST_DEFINITION.
    When LIST_CONCAT is set, lists will be prepended or appended with subsequent lists as described by
        USE_FIRST_DEFINITION (prepend if set).

        When unset, lists will be overridden by subsequent values as described by USE_FIRST_DEFINITION.
    When DEEP_MERGE, LIST_MERGE, and LIST_CONCAT are all set, lists of dicts will be merged by index and all other
        lists will be concatenated.
    """

    USE_FIRST_FILE = auto()
    DEEP_MERGE = auto()
    LIST_MERGE = auto()
    LIST_CONCAT = auto()
    USE_FIRST_DEFINITION = auto()


default_merge_type = (
    ConfigMergeType.DEEP_MERGE
    | ConfigMergeType.LIST_MERGE
    | ConfigMergeType.LIST_CONCAT
)


class ConfigParser:
    def __init__(self, model: Optional[Type[BaseModel]] = None) -> None:
        self.model = model

    def syntax_reference(self):
        """Return the configuration syntax or a reference URL"""
        raise NotImplementedError()

    def parse(self, stream: Type[TextIOBase]):
        """Return parsed config from the IO stream specified."""
        raise NotImplementedError()

    def serialize(self, config: dict) -> Union[str, bytes]:
        """Reverse the parse operation; that is, with a dictionary that represents a configuration, output the
        resulting string or bytes object that would make up a configuration file."""
        raise NotImplementedError()


class YAMLConfigParser(ConfigParser):
    pass


class TOMLConfigParser(ConfigParser):
    pass
