# Tweaking metovlogs
## Log level
The minimum log level shown by metovlogs is the first of:

* The `LOG_LEVEL` environment variable
* The `default_level` parameter
* The `DEFAULT_LEVEL` constant

For example, if you want to set the level to `INFO`:
* Environment variable: Run `export LOG_LEVEL=INFO` in your shell
* Parameter: Create your logger with `log = get_log(__name__, "INFO")`
* Constant: This should always be `DEBUG`, so that's what you get if you don't set the level

For a full list of levels, see the `coloredlogs` [documentation](https://coloredlogs.readthedocs.io/en/latest/api.html#coloredlogs.find_defined_levels) (under the hood, I use coloredlogs, so metovlogs inherits the same level names).
