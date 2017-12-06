import os
from IPython.terminal.embed import InteractiveShellEmbed
from cozmo_repl.cozmo_prompt import CozmoPrompt
import cozmo
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

# Creating IPython's history database on the main thread
ipyshell = InteractiveShellEmbed(banner1=c.bold.blue(f"\n{banner}\nWelcome to the Cozmo Shell"),
                                 exit_msg=c.bold.red("Goodbye :)\nWe Hope you had a good time with Cozmo")+"\n")


if "COZMO_LOG_LEVEL" not in os.environ:
    os.environ["COZMO_LOG_LEVEL"] = "ERROR"



def cozmo_repl(robot: cozmo.robot.Robot):
    """Invoke the ipython shell while connected to cozmo"""
    default_log_level = cozmo.logger.level
    cozmo.logger.setLevel("WARN")
    ipyshell.prompts = CozmoPrompt(ipyshell)
    ipyshell(usage)
    cozmo.logger.setLevel(default_log_level)

if __name__ == '__main__':
    cozmo.run_program(cozmo_repl, use_3d_viewer=True, use_viewer=True)
