from .gen.VUQListener import VUQListener
from .gen.VUQParser import VUQParser


class VUQInterpreter(VUQListener):
    def __init__(self, string):
        print(f"Input: {string}")

    def enterRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(ctx.getText())
