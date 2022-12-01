"""
An extension for Typer (https://github.com/tiangolo/typer) to add configuration file support to (sub)command Options.
"""

__version__ = "0.0.1"
__author__ = "Ian A. Neal"
__copyright__ = "2022 Ian A. Neal"

from typer_configparse.core import ConfigParseTyper as ConfigParseTyper
from typer_configparse.option import ConfigParseOption as ConfigParseOption
from typer_configparse.parser import ConfigParser as ConfigParser
from typer_configparse.parser import JSONConfigParser as JSONConfigParser
from typer_configparse.parser import TOMLConfigParser as TOMLConfigParser
from typer_configparse.parser import YAMLConfigParser as YAMLConfigParser

Typer = ConfigParseTyper
Option = ConfigParseOption
