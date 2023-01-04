import logging
import os

import coloredlogs

from . import lib


def get_log(name: str, default_level: str = None) -> logging.Logger:
    log = logging.getLogger(name)
    fields = [
        "{name}:{lineno}",
        "+{relativeCreated:,.0f} ms",
        "{message}",
    ]
    coloredlogs.install(
        fmt=" ".join(fields),
        style="{",
        level=default_level or lib.level_from_envar(),
        logger=log,
    )

    return log


if lib.LOG_LEVEL_ENVAR_NAME not in os.environ:
    _log = get_log(__name__)
    _log.info(
        f"To change log levels, set the environment variable LOG_LEVEL to one of: "
        + ", ".join(coloredlogs.find_defined_levels())
    )
