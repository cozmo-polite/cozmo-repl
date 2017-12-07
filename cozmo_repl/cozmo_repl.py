from IPython.terminal.embed import InteractiveShellEmbed
from cozmo_repl.cozmo_prompt import CozmoPrompt


class CozmoRepl:

    def __init__(self, cozmo, usage="", banner=None, exit_message=None, ipyshell=None):
        self.cozmo = cozmo
        self.usage = usage
        self.ipyshell = ipyshell if ipyshell else InteractiveShellEmbed(banner1=banner, exit_msg=exit_message)

    def run(self, with_viewer=False):
        def cozmo_repl(robot): # cozmo.robot.Robot
            """Invoke the ipython shell while connected to cozmo"""
            default_log_level = self.cozmo.logger.level
            self.cozmo.logger.setLevel("WARN")
            self.ipyshell.prompts = CozmoPrompt(self.ipyshell)
            self.ipyshell(self.usage)
            self.cozmo.logger.setLevel(default_log_level)

        self.cozmo.run_program(cozmo_repl, use_3d_viewer=with_viewer, use_viewer=with_viewer)
