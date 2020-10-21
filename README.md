# Intro

## Introduction
This module is based on the standard logging python module and makes use of it to implement an easy way to log to console and to a file at the same time or only one of them as you prefer.

## Usage
Very easy. First, some quick examples so you can start usind this module:

```python
import logging
from MyLogging import MyLog
log = MyLog.get_logger(
    name=__file__,
    log_level=logging.INFO
)
```

You create a log like this:
```python
log = MyLog.get_logger("mylogname")
``` 
or for example:
```
log = MyLog.get_logger(__file__)
```

This will output log messages to console and logfile. This is the default. So it will create a logfile similar to: ``` logfiles/20200107_mylogname.log ```. Note the name which is related to the "mylogname" passed as parameter. You can customize it by using the ```name="yourlogname"``` or ```name=__file__```. In case ```__file__``` as extension it will be removed.

For example, if ```name='yourfilaname.py'```, then the generated log will be ```yyyymmdd_yourfilename.log```

### Loglevel
By default de log level is DEBUG. You can override the ```log_level``` parameter to select the desired log level.

```python
log = MyLog.get_logger(
    name=__file__,
    log_level=logging.WARNING
)
```

### Logging to both console and logfile
By default log to console and file is activated. You can desactivate them by overriding the corresponnding parameted, ```log_to_console=False``` or ```log_to_file=False```
```python
log = MyLog.get_logger(__file__)
log.debug("Hello. This is a test. Thanks !")
```

### Logging to console
```python
log = MyLog.get_logger(
    log_to_file=False,
)
log.debug("Hello. This is a test. Thanks !")
```
This will output log messages only to console.

### Logging to file
```python
log = Log.get_logger(
    name="mylog",
    log_to_console=False,
)
log.debug("Hello. This is a test. Thanks !")
log.error("Hello. This is an error !")
```
This will create a logfile similar to: ``` logfiles/20200107_myfilename.log ```. Note that the file estension is eliminated.

### All possible parameters
An example with all possible parameters you can override. In the example the default values are used.
```python
import logging 
from MyLogging import MyLog

log = MyLog.get_logger(
    name=__name__,
    log_to_console = False,
    log_to_file = True,
    log_folder = 'logfiles',
    log_level = logging.DEBUG,
    log_format = '{asctime} [{levelname:5s}] [{name}] {filename:s}:{lineno:d} {message:s}',
    log_date_format = '%Y-%m-%d %H:%m',
    log_formatter = logging.Formatter(
        LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        style='{'
    ),
)
```

