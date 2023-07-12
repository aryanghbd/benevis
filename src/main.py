from lexer import Lexer

text_input = "5 ezafe 10"

lexer = Lexer().get_lexer()
toks = lexer.lex(text_input)

for tok in toks:
    print(tok)