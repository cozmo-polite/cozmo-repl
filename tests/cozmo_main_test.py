import unittest
from cozmo_repl.cozmo_main import get_repl_args


class MainTestCase(unittest.TestCase):
    def test_get_single_argument(self):
        commandline_args = ["--verbose"]
        args = get_repl_args(commandline_args)
        self.assertTrue(args.verbose)
        self.assertFalse(args.viewer)

    def test_get_complex_argument(self):
        commandline_args = ["--viewer", "--extra-paths", "yolo;toto"]
        args = get_repl_args(commandline_args)
        self.assertTrue(args.viewer)
        self.assertFalse(args.verbose)
        self.assertEqual(args.extra_paths, "yolo;toto")
