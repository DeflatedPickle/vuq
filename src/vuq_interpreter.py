from .gen.VUQListener import VUQListener
from .gen.VUQParser import VUQParser


class VUQInterpreter(VUQListener):
    def __init__(self, string):
        print(f"Input: {string}")

        self.var_dict = {}

    def enterRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Rule Block: {ctx.getText()}")

    def enterRule_match(self, ctx: VUQParser.Rule_matchContext):
        name = ctx.obj.text

        if ctx.value.INT().getText() is not None:
            value = ctx.value.INT().getText()
        elif ctx.value.CHAR().getText() is not None:
            value = self.var_dict[ctx.value.CHAR().getText()]
        elif ctx.value.VAR().getText() is not None:
            # Needs to record the function param count
            pass

        if name not in self.var_dict:
            self.var_dict[name] = value

    def exitRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Variable Dict: {self.var_dict}")
