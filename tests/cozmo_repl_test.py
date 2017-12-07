import unittest
from cozmo_repl.cozmo_repl import CozmoRepl


def noop():
    pass


class Expando(object):
    pass


class FakeCozmo:
    def __init__(self, robot=None, loggerLevel="INFO", loggerSetLevel=noop):
        self.logger = Expando()
        self.robot = robot if robot else Expando()
        self.logger.level = loggerLevel
        self.logger.setLevel = loggerSetLevel

    def run_program(self, defun, **kwargs):
        defun(self.robot)


class CheckInvocation():
    def __init__(self, testself, args):
        self.args = args
        self.testself = testself
        self.invocation = 0

    def invoke(self, args):
        invocation = self.invocation
        self.invocation += 1
        self.testself.assertEquals(args, self.args[invocation])


class ReplTestCase(unittest.TestCase):

    def test_can_create_repl_well_configurated(self):
        def ipyfake(usage):
            self.assertEqual(usage, "this is an usage")
            self.assertIsNotNone(ipyfake.prompts)

        ci = CheckInvocation(self, ["WARN", "INFO"])
        fake_cozmo = FakeCozmo(loggerSetLevel=ci.invoke)
        repl = CozmoRepl(fake_cozmo, usage="this is an usage", ipyshell=ipyfake)
        repl.run()
