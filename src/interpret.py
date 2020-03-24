import antlr4

from src.gen.VUQLexer import VUQLexer
from src.gen.VUQParser import VUQParser
from src.vuq_interpreter import VUQInterpreter


def interpret_file(string):
    lexer = VUQLexer(antlr4.FileStream(string))
    stream = antlr4.CommonTokenStream(lexer)
    parser = VUQParser(stream)
    tree = parser.start()

    listener = VUQInterpreter(string)
    antlr4.ParseTreeWalker.DEFAULT.walk(listener, tree)
