import textwrap

from .gen.VUQListener import VUQListener
from .gen.VUQParser import VUQParser


class VUQInterpreter(VUQListener):
    def __init__(self, string):
        print(f"Input: {string}")

        # Not wiped between rules
        self.var_dict = {}

        # Wiped between rules
        self.func_params = []
        # TODO: Support different comparisons and multiple rules
        self.rule = init_rule()

    def enterRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Rule Block: {ctx.getText()}")

    def enterRule_match(self, ctx: VUQParser.Rule_matchContext):
        name = ctx.obj.text

        if name not in self.var_dict:
            self.var_dict[name] = 0

        self.rule['fst'] = name
        self.rule['cmp'] = ctx.compare()

        value = ctx.value.getText()

        try:
            value = value
        except ValueError:
            if value == '|':
                value = input('> ')
            else:
                value = self.var_dict[value]

        self.rule['snd'] = int(value)

    def enterFunc(self, ctx: VUQParser.FuncContext):
        for i in ctx.CHAR():
            self.func_params.append(i.getText())

    def exitFunc_block(self, ctx: VUQParser.Func_blockContext):
        print(f"Params List: {self.func_params}")

        exec(textwrap.dedent(f"""
        while not ({self.var_dict[self.rule['fst']]}\
                    {comparison_to_expression(self.rule['cmp'])}\
                    {int(self.rule['snd'])}):
            for i in ctx.expression():
                i.enterRule(self)
        """))

    def enterOutput(self, ctx: VUQParser.OutputContext):
        print(
            self.var_dict[
                self.func_params[
                    str(ctx.var().getText()).count(',') - 1
                    ]
            ],
            end=print('' if ctx.END_LINE() is None else '\n'))

    # def enterExpression(self, ctx:VUQParser.ExpressionContext):
    #     print(comparison_to_expression(self.rule['cmp']), self.var_dict, self.func_params)

    def enterArith(self, ctx: VUQParser.ArithContext):
        # Gets the func parameter matching the index of the number of commas
        first = self.func_params[
            str(ctx.first.getText()).count(',') - 1
            ]

        op = ctx.arithOp().getText()

        try:
            # It's a normal number
            value = float(ctx.second.getText())
        except ValueError:
            s = ctx.second.getText()

            if s in self.var_dict:
                # It's a variable
                value = self.var_dict[s]
            elif s == len(s) * s[0]:
                # It's all commas
                value = float(
                    self.var_dict[
                        self.func_params[
                            str(ctx.second.getText()).count(',') - 1
                            ]
                    ]
                )

        exec(f"self.var_dict[first] = {self.var_dict[first]} {op} {value}")

    def exitRule_block(self, ctx: VUQParser.Rule_blockContext):
        print(f"Variable Dict: {self.var_dict}")

        for k, v in self.var_dict.items():
            self.var_dict[k] = 0

        self.func_params.clear()
        self.rule = init_rule()


def init_rule():
    return {
        'fst': 0,
        'cmp': '',
        'snd': 0
    }


# This is a mess, but I couldn't think right
def comparison_to_expression(comp: VUQParser.CompareContext):
    builder = []

    if comp.LESS() is not None:
        if comp.NOT() is not None:
            builder.append('>')
        else:
            builder.append('<')
    else:
        if comp.NOT() is not None:
            builder.append('!')

    if comp.EQUALS() is not None:
        builder.append('=')

        if comp.LESS() is None:
            builder.append('=')

    print(f"Comparison: {builder}")
    return ''.join(builder)
