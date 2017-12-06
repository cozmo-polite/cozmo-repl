import sys
from IPython.terminal.embed import InteractiveShellEmbed
from IPython.terminal.prompts import Prompts, Token
import cozmo
import style as c

usage = f"""\
This is an {c.bold.cyan('IPython')} interactive shell for {c.bold.blue('Cozmo')}.
All commands are executed within cozmo's running program loop.
Use the [tab] key to auto-complete commands, and see all available methods.
All IPython commands work as usual. See below for some useful syntax:
  {c.bold.cyan('?')}         -> Introduction and overview of IPython's features.
  {c.bold.cyan('object?')}   -> Details about 'object'.
  {c.bold.cyan('object??')}  -> More detailed, verbose information about 'object'.\
  """

# Creating IPython's history database on the main thread
ipyshell = InteractiveShellEmbed(banner1=c.bold.blue("\nWelcome to the Cozmo Shell"),
                                 exit_msg=c.bold.red("Goodbye")+"\n")


def cozmo_repl(robot: cozmo.robot.Robot):
    """Invoke the ipython shell while connected to cozmo"""
    default_log_level = cozmo.logger.level
    cozmo.logger.setLevel('WARN')
    ipyshell(usage)
    cozmo.logger.setLevel(default_log_level)

if __name__ == '__main__':
    cozmo.run_program(cozmo_repl, use_3d_viewer=True, use_viewer=True)