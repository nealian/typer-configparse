from enum import IntEnum
from typing import Any, Callable, Dict, List, Optional, Type, Union

import typer
import typer.core

from typer_configparse.option import ConfigParseOption
from typer_configparse.parser import ConfigParser


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
        name: Optional[str] = typer.models.Default(None),
        cls: Optional[Type[typer.core.TyperGroup]] = typer.models.Default(None),
        invoke_without_command: bool = typer.models.Default(False),
        no_args_is_help: bool = typer.models.Default(False),
        subcommand_metavar: Optional[str] = typer.models.Default(None),
        chain: bool = typer.models.Default(False),
        result_callback: Optional[Callable[..., Any]] = typer.models.Default(None),
        context_settings: Optional[Dict[Any, Any]] = typer.models.Default(None),
        callback: Optional[Callable[..., Any]] = typer.models.Default(None),
        help: Optional[str] = typer.models.Default(None),
        epilog: Optional[str] = typer.models.Default(None),
        short_help: Optional[str] = typer.models.Default(None),
        options_metavar: str = typer.models.Default("[OPTIONS]"),
        add_help_option: bool = typer.models.Default(True),
        hidden: bool = typer.models.Default(False),
        deprecated: bool = typer.models.Default(False),
        add_completion: bool = True,
        rich_markup_mode: typer.core.MarkupMode = None,
        rich_help_panel: Union[str, None] = typer.models.Default(None),
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
        # Our options
        config_file_base_name: Optional[str] = typer.models.Default(None),
        config_file: Optional[str] = typer.models.Default(None),
        config_files: Optional[List[str]] = typer.models.Default(None),
        config_file_search_paths: Optional[List[str]] = typer.models.Default(None),
        config_file_extensions: Optional[List[str]] = typer.models.Default(None),
        config_file_section: Optional[str] = typer.models.Default(None),
        config_parsers: List[Type[ConfigParser]] = [],
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


Typer = ConfigParseTyper
Option = ConfigParseOption
