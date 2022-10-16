# metovlogs

> Dead simple Python logging.

metovlogs is a very simple logging library. Setup is one line, then you can use it as a drop-in `print` replacement. Sane and useful log format out of the box. Best for small or early stage projects.

## Usage
Initialize the logger by calling `get_log`:
```
import metovlogs

# The name will be used to annotate the log
# __name__ is name of the current Python module
log = metovlogs.get_log(__name__)
```

Now you can use it as a drop-in replacement for all your `print`s:
```
# Do some stuff
log.info("Finished doing some stuff")

log.debug("About to start doing other stuff")
# Do some other stuff
```

metovlogs is like [black](https://github.com/psf/black) for logs: You get reasonable behavior by default and [minimal customization](doc/tweaks.md). This allows you to focus on developing without distraction. If you want to customize your logs more, you should use something else.

## Installation

```
pip install metovlogs
```

## Further reading

* [Background](doc/background.md)
* [Contribution guidelines](doc/contributing.md)
* [Planned future work](doc/todo.md)
