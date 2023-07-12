from lexer import Lexer
from parser import Parser

text_input = "5 menhaye 10"

lexer = Lexer().get_lexer()
parser = Parser(lexer)
parser.parse()
pg = parser.get_parser()

tokens = lexer.lex(text_input)
res = pg.parse(tokens)

print(res.evaluate())