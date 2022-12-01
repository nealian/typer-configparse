from enum import Flag, auto
from io import TextIOBase
from typing import Any, Dict, Optional, Type, Union

import toml
import yaml
import json
from attrdict import AttrDict
from pydantic import BaseModel, create_model_from_typeddict
from typing_extensions import TypedDict


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
    def __init__(
        self, model: Union[None, Type[BaseModel], Type[TypedDict]] = None
    ) -> None:
        self.model = model
        if model is not None and issubclass(model, TypedDict):
            self.model = create_model_from_typeddict(model)

    @staticmethod
    def syntax_reference() -> str:
        """Return the configuration syntax or a reference URL"""
        raise NotImplementedError()

    def parse(self, stream: Union[TextIOBase, str, bytes]) -> Union[AttrDict, dict]:
        """Return parsed config (as a dict or AttrDict) from the IO stream specified."""
        raise NotImplementedError()

    def serialize(self, config: Union[dict, AttrDict]) -> Union[str, bytes]:
        """Reverse the parse operation; that is, with a dictionary that represents a configuration, output the
        resulting string or bytes object that would make up a configuration file."""
        raise NotImplementedError()

    def validate(self, config: Union[dict, AttrDict]) -> Optional[BaseModel]:
        """Validate config against model defined in __init__ (and return an instance if valid)."""
        if isinstance(self.model, BaseModel):
            return self.model.validate(config)


class YAMLConfigParser(ConfigParser):
    @staticmethod
    def syntax_reference() -> str:
        return "https://yaml.org/"

    def parse(self, stream: Union[TextIOBase, str, bytes]) -> AttrDict:
        _data = stream
        if isinstance(stream, TextIOBase):
            with stream:
                _data = stream.read()
        return AttrDict(yaml.load(_data, Loader=yaml.SafeLoader))

    def serialize(self, config: Union[dict, AttrDict]) -> str:
        return yaml.dump(dict(config), Dumper=yaml.SafeDumper)


class TOMLConfigParser(ConfigParser):
    @staticmethod
    def syntax_reference() -> str:
        return "https://toml.io/en/"

    def parse(
        self,
        stream: Union[TextIOBase, str],
        /,
        _dict: Type[Dict[str, Any]] = AttrDict,
    ) -> Dict[str, Any]:
        _data = stream
        if isinstance(stream, TextIOBase):
            with stream:
                _data = stream.read()
        return toml.loads(_data, _dict=_dict)  # type: ignore

    def serialize(self, config: Union[dict, AttrDict]) -> str:
        return toml.dumps(config)


class JSONConfigParser(ConfigParser):
    @staticmethod
    def syntax_reference() -> str:
        return "https://www.json.org/json-en.html"

    def parse(
        self,
        stream: Union[TextIOBase, str, bytes],
        /,
        _dict: Type[Dict[str, Any]] = AttrDict,
    ) -> Dict[str, Any]:
        _data = stream
        if isinstance(stream, TextIOBase):
            with stream:
                _data = stream.read()
        return json.loads(_data, object_hook=_dict)  # type: ignore

    def serialize(
        self,
        config: Union[dict, AttrDict],
        /,
        indent: Union[int, str, None] = 4,
        sort_keys: bool = True,
    ) -> str:
        return json.dumps(config, indent=indent, sort_keys=sort_keys)
