import unittest
from cozmo_repl.cozmo_repl import CozmoRepl
from .tests_utils import CheckInvocation, FakeCozmo


class ReplTestCase(unittest.TestCase):

    def test_can_create_repl_well_configurated(self):
        def ipyfake(usage):
            self.assertEqual(usage, "this is an usage")
            self.assertIsNotNone(ipyfake.prompts)

        ci = CheckInvocation(self, ["WARN", "INFO"])
        fake_cozmo = FakeCozmo(loggerSetLevel=ci.invoke)
        repl = CozmoRepl(fake_cozmo, usage="this is an usage", ipyshell=ipyfake)
        repl.run()
