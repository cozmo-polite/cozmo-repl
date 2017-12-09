from IPython.terminal.embed import InteractiveShellEmbed
from cozmo_repl.cozmo_prompt import CozmoPrompt

class CozmoRepl:

    def __init__(self, cozmo, usage="", banner="", exit_message="",
                 ipyshell=None, path=None):
        self.cozmo = cozmo
        self.usage = usage
        self.ipyshell = ipyshell if ipyshell else InteractiveShellEmbed(banner1=banner, exit_msg=exit_message)
        self.path = path if path else []
        self.default_log_level = self.cozmo.logger.level

    def add_path(self, extra_paths):
        self.path.append(".")
        if extra_paths:
            for extra_path in extra_paths.split(";"):
                self.path.append(extra_path)

    def run(self, with_viewer=False, verbose=False, extra_paths=None):
        def cozmo_repl(robot): # cozmo.robot.Robot
            """Invoke the ipython shell while connected to cozmo"""
            self.cozmo.logger_protocol.disabled = self.cozmo.logger.disabled = False
            self.cozmo.logger.setLevel("WARN")
            self.ipyshell.prompts = CozmoPrompt(self.ipyshell)
            self.ipyshell(self.usage)
            self.cozmo.logger.setLevel(self.default_log_level)

        if not verbose:
            self.cozmo.logger_protocol.disabled = self.cozmo.logger.disabled = True

        self.add_path(extra_paths)

        self.cozmo.run_program(cozmo_repl, use_3d_viewer=with_viewer, use_viewer=with_viewer)
