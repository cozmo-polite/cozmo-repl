import unittest
from cozmo_repl.cozmo_repl import CozmoRepl
from .tests_utils import CheckInvocation, FakeCozmo


class ReplTestCase(unittest.TestCase):

    def test_can_create_repl_well_configurated(self):
        def ipyfake(usage):
            self.assertEqual(usage, "this is an usage")
            self.assertIsNotNone(ipyfake.prompts)

        ci = CheckInvocation(self, ["WARN", "INFO"])
        fake_cozmo = FakeCozmo(
            logger_set_level=ci.invoke,
            pre_check=lambda cozmo_self: self.assertTrue(cozmo_self.logger.disabled),
            post_check=lambda cozmo_self: self.assertFalse(cozmo_self.logger.disabled)
        )
        repl = CozmoRepl(fake_cozmo, usage="this is an usage", ipyshell=ipyfake)
        repl.run()

    def test_can_create_repl_well_configurated_verbose(self):
        def ipyfake(usage):
            self.assertEqual(usage, "this is an usage")
            self.assertIsNotNone(ipyfake.prompts)

        ci = CheckInvocation(self, ["WARN", "INFO"])
        fake_cozmo = FakeCozmo(
            logger_set_level=ci.invoke,
            pre_check=lambda cozmo_self: self.assertFalse(cozmo_self.logger.disabled),
            post_check=lambda cozmo_self: self.assertFalse(cozmo_self.logger.disabled)
        )
        repl = CozmoRepl(fake_cozmo, usage="this is an usage", ipyshell=ipyfake)
        repl.run(verbose=True)
