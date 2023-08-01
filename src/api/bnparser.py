from rply import ParserGenerator
from primitives import binaryops, integer, conditionals, variable, misc, program

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.pg = ParserGenerator(
            ['CHIYE', 'ASSIGNMENT', 'INTEGER', 'VARIABLE', 'AGAR', 'DAR_GHEYRE_IN_SOORAT', 'BARAYE', 'TA', 'BE_ALAVEYE_LA', 'BE_ALAVEYE_FA', 'PLUS', 'MENHAYE_LA', 'MENHAYE_FA', 'MINUS', 'ZARBDARE_LA', 'ZARBDARE_FA', 'MULTIPLY', 'TAGHSIM_BAR_LA', 'TAGHSIM_BAR_FA', 'DIVIDE', 'MOSAVIYE_LA', 'MOSAVIYE_FA', 'EQUAL', 'MOSAVI_NIST_BA', 'NEQ', 'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACE', 'CLOSE_BRACE']
        )

    def parse(self):

        @self.pg.production('program : statement')
        @self.pg.production('program : statement program')
        def prog(p):
            return program.Program([p[0]] + p[1:])

        @self.pg.production('term : INTEGER')
        @self.pg.production('term : VARIABLE')


        def term(p):
            if p[0].gettokentype() == "VARIABLE":
                return variable.Variable(p[0].getstr())
            else:
                return integer.Integer(int(p[0].getstr()))


        @self.pg.production('statement : VARIABLE ASSIGNMENT expression')
        def statement_assignment(p):
            return variable.Assignment(p[0], p[2])

        @self.pg.production('statement : CHIYE OPEN_PAREN expression CLOSE_PAREN')
        def statement_print(p):
            return misc.Print(p[2])

        @self.pg.production('statement : AGAR expression statement DAR_GHEYRE_IN_SOORAT statement')
        def statement_conditional(p):
            return conditionals.Conditional(p[1], p[2], p[4])

        @self.pg.production('statement : AGAR expression statement')
        def statement_basicconditional(p):
            return conditionals.Conditional(p[1], p[2], None)

        @self.pg.production('statement : TA expression statement')
        def statement_while(p):
            return conditionals.While(p[1], p[2])

        @self.pg.production('expression : term')
        @self.pg.production('expression : VARIABLE')
        @self.pg.production('expression : expression PLUS term')
        @self.pg.production('expression : expression BE_ALAVEYE_LA term')
        @self.pg.production('expression : expression BE_ALAVEYE_FA term')
        @self.pg.production('expression : expression MINUS term')
        @self.pg.production('expression : expression MENHAYE_LA term')
        @self.pg.production('expression : expression MENHAYE_FA term')

        def expression(p):
            if len(p) == 1:
                return p[0]
            else:
                larg = p[0]
                rarg = p[2]
                operator = p[1].gettokentype()

                if operator in ['PLUS', 'BE_ALAVEYE_LA', 'BE_ALAVEYE_FA']:
                    return binaryops.Add(larg, rarg)
                elif operator in ['MINUS', 'MENHAYE_LA', 'MENHAYE_FA']:
                    return binaryops.Subtract(larg, rarg)



        @self.pg.error
        def error_handler(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
