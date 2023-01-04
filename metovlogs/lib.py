import os

import coloredlogs

DEFAULT_LEVEL = "DEBUG"
LOG_LEVEL_ENVAR_NAME = "LOG_LEVEL"


def level_from_envar():
    """
    Read log level from environment variable.
    """
    level = os.environ.get(LOG_LEVEL_ENVAR_NAME)
    if level not in coloredlogs.find_defined_levels():
        level = DEFAULT_LEVEL
    return level
