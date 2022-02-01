import logging
import coloredlogs


def get_log(name: str) -> logging.Logger:
    log = logging.getLogger(name)
    fields = [
        "{name}:{lineno}",
        "+{relativeCreated:,.0f} ms",
        "{message}",
    ]
    coloredlogs.install(fmt=" ".join(fields), style="{", level="DEBUG", logger=log)
    return log
