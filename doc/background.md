# Background
Python has very powerful logging capabilities, but the default log configuration is not particularly good and having to set up the logs for every project can be tedious. I decided to make metovlogs to solve this problem. It has very little customization and sane defaults, which means there's nothing to set up. There's just one line to initialize the log. This makes it great for small, early-stage projects where you just want to get decent logging with minimal effort.

At some point your project might evolve to the point where metovlogs is not sufficient and you need to customize the logging more. This is when you can remove metovlogs from your project and set up a more sophisticated logging system. But while you are getting to that point, metovlogs allows you to log with as little effort as just `print`ing things.

## Why not just `print`?
`print` sends the message to standard out, which is more appropriate for actual output from your program (hence the name). Using `print` for diagnostics pollutes standard output and makes it hard to follow the Unix philosophy.

Say you have a program `foo` that produces JSON data as output. You can do things like:
```shell
# Take the "url" key of each array element and download it
foo | jq ".[].url" | xargs wget
```

But if you also `print` messages like "Generating URL for item X..." into standard output, `jq` will give you an error and you will have to do a bunch of busywork to clean up the output. You can avoid this by sending your messages to standard error, which is not passed over by `|` but instead gets printed to the terminal for the user to see. Loggers normally print to STDERR.

## Justification for defaults
### Debug by default
By default, metovlogs shows levels down to `DEBUG`. This is a useful level, so we don't hide it. Note that log levels are inherited from `coloredlogs`, so there are levels lower than `DEBUG`, like `SPAM`.

### Colors
Under the hood, metovlogs uses `coloredlogs` which uses color to show message severity and highlight different metadata fields. The colors make it easy to quickly scan the log by eye. They also make the logs prettier and more fun.

`coloredlogs` inserts ASCII control characters to indicate color. If your in an enviornment where color doesn't make sense it should normally just detect it and omit colors. If you have a lot of problems with gibberish characters in logs, it's probably worth your time to set up a more customized logger.

### Execution time
The logs indicate milliseconds since the program's start. You can use this to locate performance bottlenecks and get an idea of timing in general.

### No absolute timestamps
By default, there is no date and time in logs, because it is rarely important for early stage projects.
