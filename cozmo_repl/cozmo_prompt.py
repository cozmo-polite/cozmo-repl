from IPython.terminal.prompts import Prompts, Token


class CozmoPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [(Token.Prompt, '>>> ')]
        # TODO: find a cozmo status!

    def out_prompt_tokens(self):
        return [(Token.Prompt, '<<< ')]
