from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Type, Union

import typer
import typer.core

from typer_configparse.option import ConfigParseArgument, ConfigParseOption
from typer_configparse.parser import (
    ConfigParser,
    JSONConfigParser,
    TOMLConfigParser,
    YAMLConfigParser,
)

Default = typer.models.Default


def isdefault(var: Any):
    return isinstance(var, typer.models.DefaultPlaceholder)


class ConfigSource(IntEnum):
    COMMAND_LINE = 0
    ENVIRONMENT = 1
    CONFIG_FILE = 2
    DEFAULT = 3


class ConfigReader:
    def __init__(
        self,
    ) -> None:
        pass


class ConfigParseTyper(typer.Typer):
    def __init__(
        self,
        *,
        # Upstream (Typer) options
        name: Optional[str] = Default(None),
        cls: Optional[Type[typer.core.TyperGroup]] = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Optional[str] = Default(None),
        chain: bool = Default(False),
        result_callback: Optional[Callable[..., Any]] = Default(None),
        context_settings: Optional[Dict[Any, Any]] = Default(None),
        callback: Optional[Callable[..., Any]] = Default(None),
        help: Optional[str] = Default(None),
        epilog: Optional[str] = Default(None),
        short_help: Optional[str] = Default(None),
        options_metavar: str = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        add_completion: bool = True,
        rich_markup_mode: typer.core.MarkupMode = None,
        rich_help_panel: Union[str, None] = Default(None),
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
        # Our options
        config_file_base_name: Optional[str] = Default(None),
        config_file: Optional[str] = Default(None),
        config_files: Optional[List[str]] = Default(None),
        config_file_search_paths: Optional[List[str]] = Default(None),
        config_file_extensions: Optional[List[str]] = Default(None),
        config_file_section: Optional[str] = Default(None),
        config_parsers: List[Type[ConfigParser]] = Default([]),
        option_source_precedence: List[ConfigSource] = [
            ConfigSource.DEFAULT,
            ConfigSource.CONFIG_FILE,
            ConfigSource.ENVIRONMENT,
            ConfigSource.COMMAND_LINE,
        ],
    ) -> None:
        super().__init__(
            name=name,
            cls=cls,
            invoke_without_command=invoke_without_command,
            no_args_is_help=no_args_is_help,
            subcommand_metavar=subcommand_metavar,
            chain=chain,
            result_callback=result_callback,
            context_settings=context_settings,
            callback=callback,
            help=help,
            epilog=epilog,
            short_help=short_help,
            options_metavar=options_metavar,
            add_help_option=add_help_option,
            hidden=hidden,
            deprecated=deprecated,
            add_completion=add_completion,
            rich_markup_mode=rich_markup_mode,
            rich_help_panel=rich_help_panel,
            pretty_exceptions_enable=pretty_exceptions_enable,
            pretty_exceptions_show_locals=pretty_exceptions_show_locals,
            pretty_exceptions_short=pretty_exceptions_short,
        )
        self.config_file_base_name = (
            config_file_base_name if not isdefault(config_file_base_name) else name
        )
        self.config_files = (
            config_files
            if not isdefault(config_files)
            else [config_file]
            if not isdefault(config_file)
            else None  # FIXME?
        )
        self.config_file_search_paths = (
            config_file_search_paths
            if not isdefault(config_file_search_paths)
            else None  # FIXME
        )
        self.config_file_extensions = (
            config_file_extensions
            if not isdefault(config_file_extensions)
            else None  # FIXME?
        )
        self.config_file_section = (
            config_file_section
            if not isdefault(config_file_section)
            else "__ROOT__"  # FIXME?
        )
        self.config_parsers = (
            config_parsers
            if not isdefault(config_parsers)
            else [YAMLConfigParser, TOMLConfigParser, JSONConfigParser]
        )
        self.option_source_precedence = option_source_precedence

    def callback(
        self,
        name: Optional[str] = Default(None),
        *,
        cls: Optional[Type[typer.core.TyperGroup]] = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Optional[str] = Default(None),
        chain: bool = Default(False),
        result_callback: Optional[Callable[..., Any]] = Default(None),
        context_settings: Optional[Dict[Any, Any]] = Default(None),
        help: Optional[str] = Default(None),
        epilog: Optional[str] = Default(None),
        short_help: Optional[str] = Default(None),
        options_metavar: str = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        rich_help_panel: Union[str, None] = Default(None),
    ) -> Callable[[typer.models.CommandFunctionType], typer.models.CommandFunctionType]:
        return super().callback(
            name=name,
            cls=cls,
            invoke_without_command=invoke_without_command,
            no_args_is_help=no_args_is_help,
            subcommand_metavar=subcommand_metavar,
            chain=chain,
            result_callback=result_callback,
            context_settings=context_settings,
            help=help,
            epilog=epilog,
            short_help=short_help,
            options_metavar=options_metavar,
            add_help_option=add_help_option,
            hidden=hidden,
            deprecated=deprecated,
            rich_help_panel=rich_help_panel,
        )
        # TODO

    def add_typer(
        self,
        typer_instance: "Typer",
        *,
        name: Optional[str] = ...,
        cls: Optional[Type[typer.core.TyperGroup]] = ...,
        invoke_without_command: bool = ...,
        no_args_is_help: bool = ...,
        subcommand_metavar: Optional[str] = ...,
        chain: bool = ...,
        result_callback: Optional[Callable[..., Any]] = ...,
        context_settings: Optional[Dict[Any, Any]] = ...,
        callback: Optional[Callable[..., Any]] = ...,
        help: Optional[str] = ...,
        epilog: Optional[str] = ...,
        short_help: Optional[str] = ...,
        options_metavar: str = ...,
        add_help_option: bool = ...,
        hidden: bool = ...,
        deprecated: bool = ...,
        rich_help_panel: Union[str, None] = ...,
    ) -> None:
        return super().add_typer(
            typer_instance,
            name=name,
            cls=cls,
            invoke_without_command=invoke_without_command,
            no_args_is_help=no_args_is_help,
            subcommand_metavar=subcommand_metavar,
            chain=chain,
            result_callback=result_callback,
            context_settings=context_settings,
            callback=callback,
            help=help,
            epilog=epilog,
            short_help=short_help,
            options_metavar=options_metavar,
            add_help_option=add_help_option,
            hidden=hidden,
            deprecated=deprecated,
            rich_help_panel=rich_help_panel,
        )
        # TODO

    def command(
        self,
        name: Optional[str] = None,
        *,
        cls: Optional[Type[typer.core.TyperCommand]] = None,
        context_settings: Optional[Dict[Any, Any]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_help_panel: Union[str, None] = ...,
    ) -> Callable[[typer.models.CommandFunctionType], typer.models.CommandFunctionType]:
        return super().command(
            name,
            cls=cls,
            context_settings=context_settings,
            help=help,
            epilog=epilog,
            short_help=short_help,
            options_metavar=options_metavar,
            add_help_option=add_help_option,
            no_args_is_help=no_args_is_help,
            hidden=hidden,
            deprecated=deprecated,
            rich_help_panel=rich_help_panel,
        )
        # TODO

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        val = super().__call__(*args, **kwargs)
        # TODO
        return val


Typer = ConfigParseTyper
Option = ConfigParseOption
