from .cozmo_repl import CozmoRepl
import cozmo
import argparse
import os
import sys
import style as c

banner = """\
   ______                               ____             __
  / ____/___  ____  ____ ___  ____     / __ \___  ____  / /
 / /   / __ \/_  / / __ `__ \/ __ \   / /_/ / _ \/ __ \/ /
/ /___/ /_/ / / /_/ / / / / / /_/ /  / _, _/  __/ /_/ / /
\____/\____/ /___/_/ /_/ /_/\____/  /_/ |_|\___/ .___/_/
                                              /_/
"""

usage = f"""\
This is an {c.bold.cyan('IPython')} interactive shell for {c.bold.blue('Cozmo')}.
All commands are executed within cozmo's running program loop.
Use the [tab] key to auto-complete commands, and see all available methods.
All IPython commands work as usual. See below for some useful syntax:
  {c.bold.cyan('?')}         -> Introduction and overview of IPython's features.
  {c.bold.cyan('object?')}   -> Details about 'object'.
  {c.bold.cyan('object??')}  -> More detailed, verbose information about 'object'.\
  """

REPL = CozmoRepl(cozmo, path=sys.path, usage=usage,
                 banner=c.bold.blue(f"\n{banner}\nWelcome to the Cozmo Shell"),
                 exit_message=c.bold.red("Goodbye :)\nWe Hope you had a good time with Cozmo\n"))

if "COZMO_LOG_LEVEL" not in os.environ:
    os.environ["COZMO_LOG_LEVEL"] = "ERROR"


def get_repl_args(commandline_args=None):
    parser = argparse.ArgumentParser(description="Cozmo Repl")
    parser.add_argument("--viewer", help="Launch with viewer", action="store_true", required=False)
    parser.add_argument("--verbose", help="Verbose mode", action="store_true", required=False)
    parser.add_argument("--extra-paths", help="Directories to add to import path (; separated)", metavar="p", required=False)
    args = parser.parse_args(commandline_args)
    return args
