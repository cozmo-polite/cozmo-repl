Cozmo REPL
==========

[![PyPI](https://img.shields.io/pypi/v/cozmo-repl.svg)](https://pypi.python.org/pypi/cozmo-repl)
[![Build Status](https://travis-ci.org/cozmo-polite/cozmo-repl.svg?branch=master)](https://travis-ci.org/cozmo-polite/cozmo-repl)
[![Codecov](https://img.shields.io/codecov/c/github/cozmo-polite/cozmo-repl.svg)](https://codecov.io/gh/cozmo-polite/cozmo-repl)

> IPython REPL for the [Cozmo][cozmo] Robot

## Installation

Just use `pip`:

```sh
pip install cozmo-repl
```

This takes care to install all the dependencies of cozmo

## Usage

Just connect your phone to your computer and your cozmo and run
`cozmo-repl`.

This open a IPython REPL in the context of a Cozmo program giving you
access to `robot` and hence control over Cozmo. For full reference of
the `cozmo` API go over [here][cozmo-api]

It takes care to add the current directly in the python path, but it's
also possible to specify extra paths with the `--extra-paths` option 
in case you need it.

By default it opens without viewer attached to cozmo (its camera, and
a 3D representation of its world). To activate them, just add the
`--viewer` flag in the command line.

For a complete overview of available options, just run `cozmo-repl --help`

[cozmo]: https://www.anki.com/en-us/cozmo
[cozmo-api]: http://cozmosdk.anki.com/docs/api.html
