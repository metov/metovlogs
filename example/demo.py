from pathlib import Path

from metovlogs import get_log

log = get_log(Path(__file__).name)

log.debug("example of event that is only interesting when debugging")
log.info("example of a normal event, that the user might want to know about")
log.warning("example of something that may be bad, but the user should decide")
log.error("example of something bad, but program can continue and recover")
log.critical("example of something very bad, program cannot continue")
