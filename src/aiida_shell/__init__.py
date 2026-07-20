"""AiiDA plugin that makes running shell commands easy."""

__version__ = '0.8.2'

from .calculations import ShellJob
from .data import EntryPointData, PickledData, ShellCode
from .launch import launch_shell_job
from .parsers import ShellParser

__all__ = (
    'EntryPointData',
    'PickledData',
    'ShellCode',
    'ShellJob',
    'ShellParser',
    'launch_shell_job',
)
