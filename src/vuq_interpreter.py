from .gen.VUQListener import VUQListener
from .gen.VUQParser import VUQParser


class VUQInterpreter(VUQListener):
    def __init__(self, string):
        print(f"Input: {string}")

        self.var_dict = {}
        self.func_params = []

    def enterRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Rule Block: {ctx.getText()}")

    def enterRule_match(self, ctx: VUQParser.Rule_matchContext):
        name = ctx.obj.text

        if name not in self.var_dict:
            # if ctx.value.INT().getText() is not None:
            #     value = ctx.value.INT().getText()
            # elif ctx.value.CHAR().getText() is not None:
            #     value = self.var_dict[ctx.value.CHAR().getText()]

            self.var_dict[name] = 0

    def enterFunc(self, ctx: VUQParser.FuncContext):
        self.func_params.clear()

        for i in ctx.CHAR():
            self.func_params.append(i.getText())

    def enterArith(self, ctx: VUQParser.ArithContext):
        op = ctx.arithOp().getText()

        first = self.func_params[str(ctx.first.getText()).count(",") - 1]

        try:
            value = float(ctx.second.getText())
        except ValueError:
            s = ctx.second.getText()
            
            if s in self.var_dict:
                # It's a variable
                value = self.var_dict[s]
            elif s == len(s) * s[0]:
                # It's all commas
                value = float(self.var_dict[self.func_params[str(ctx.second.getText()).count(",") - 1]])

        if op == "+":
            self.var_dict[first] = self.var_dict[first] + value
        elif op == "-":
            self.var_dict[first] = self.var_dict[first] - value
        elif op == "*":
            self.var_dict[first] = self.var_dict[first] * value
        elif op == "/":
            self.var_dict[first] = self.var_dict[first] / value

    def exitRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Variable Dict: {self.var_dict}")
        print(f"Params List: {self.func_params}")
