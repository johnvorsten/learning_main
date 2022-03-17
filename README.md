## Build instructions

## What does the -m switch do?
From the [docs](https://docs.python.org/3/using/cmdline.html#cmdoption-m): Search sys.path for the named module and execute its contents as the __main__ module.


## Motivation

Calling a module with the -m switch:

Calling a package with the -m switch:
Package names are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute <pkg>.__main__ as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.