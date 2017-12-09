import unittest
from cozmo_repl.cozmo_prompt import CozmoPrompt


class PromptTestCase(unittest.TestCase):
    """So far dummy test about the prompt"""
    def test_in_prompt(self):
        prompt = CozmoPrompt(None)
        inp = prompt.in_prompt_tokens()
        self.assertEqual(inp[0][1], '>>> ')

    def test_out_prompt(self):
        prompt = CozmoPrompt(None)
        outp = prompt.out_prompt_tokens()
        self.assertEqual(outp[0][1], '<<< ')
