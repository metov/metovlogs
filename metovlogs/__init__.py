import logging
import coloredlogs

from . import lib


def get_log(name: str) -> logging.Logger:
    log = logging.getLogger(name)
    fields = [
        "{name}:{lineno}",
        "+{relativeCreated:,.0f} ms",
        "{message}",
    ]
    coloredlogs.install(
        fmt=" ".join(fields),
        style="{",
        level=lib.level_from_envar(),
        logger=log,
    )
    return log
