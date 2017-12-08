import unittest
from cozmo_repl.cozmo_repl import CozmoRepl


def noop(*args, **kwargs):
    pass


class Expando: pass


class FakeLogger:
    def __init__(self, level="INFO", setLevel=noop):
        self.disabled = False
        self.level = level
        self.setLevel = setLevel


class FakeCozmo:
    def __init__(self, robot=None, logger_level="INFO", logger_set_level=noop, pre_check=noop, post_check=noop):
        self.logger = FakeLogger(logger_level, logger_set_level)
        self.logger_protocol = FakeLogger()
        self.robot = robot if robot else Expando()

        self.pre_check = pre_check
        self.post_check = post_check

    def run_program(self, defun, **kwargs):
        self.pre_check(self)
        defun(self.robot)
        self.post_check(self)


class CheckInvocation():
    def __init__(self, test_self, args):
        self.args = args
        self.testself = test_self
        self.invocation = 0

    def invoke(self, args):
        invocation = self.invocation
        self.invocation += 1
        self.testself.assertEquals(args, self.args[invocation])
