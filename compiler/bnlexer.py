from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()


    def _add_tokens(self):
        ##need b' so that we don't accidentally pick up the entire phrase as a substr when lexing

        '''
        Initial Keywords
            -Things like if, for, else, while
            -Note that for all terms and operators we have pinglish and farsi script parsed equivalently
        '''
        self.lexer.add('AGAR_LA', r'\bagar\b')
        self.lexer.add('AGAR_FA', r'\bاگر\b')

        self.lexer.add('DAR_GHEYRE_IN_SOORAT_LA', r'\bdar gheyre in soorat\b')
        self.lexer.add('DAR_GHEYRE_IN_SOORAT_FA', r'\bدر غیر این صورت\b')

        self.lexer.add('BARAYE_LA', r'\bbaraye\b')
        self.lexer.add('BARAYE_FA', r'\bبرای\b')

        self.lexer.add('TA_LA', r'\bta\b')
        self.lexer.add('TA_FA', r'\bتا\b')


        '''
        Operators
            -Things like +, -, *, /
            -Note that we can use words or the actual symbols for these, so each one comes as a pair (treated the same in AST)
        '''
        self.lexer.add('BE_ALAVEYE_LA', r'\bbe alaveye\b')
        self.lexer.add('BE_ALAVEYE_FA', r'\bبه علاوه\b')
        self.lexer.add('PLUS', r'\+')

        self.lexer.add('MENHAYE_LA', r'\bmenhaye\b')
        self.lexer.add('MENHAYE_FA', r'\bمنهای\b')
        self.lexer.add('MINUS', r'\-')

        self.lexer.add('ZARBDARE_LA', r'\bzarbdare\b')
        self.lexer.add('ZARBDARE_FA', r'\b ضرب در\b')
        self.lexer.add('MULTIPLY', r'\*')

        self.lexer.add('TAGHSIM_BAR_LA', r'\btaghsim bar\b')
        self.lexer.add('TAGHSIM_BAR_FA', r'\bتقسیم بر\b')
        self.lexer.add('DIVIDE', r'\\')

        self.lexer.add('MOSAVIYE_LA', r'\bmosaviye\b')
        self.lexer.add('MOSAVIYE_FA', r'\bمساوی\b')
        self.lexer.add('EQUAL', r'\==')

        self.lexer.add('MOSAVI_NIST_BA_LA', r'\bmosavi nist ba\b')
        self.lexer.add('MOSAVI_NIST_BA_FA', r'\bمساوی نیست با\b')
        self.lexer.add('NEQ', r'\!=')

        self.lexer.add('ASSIGNMENT', r'=')
        self.lexer.add('CHIYE', r'\bchiye\b')

        '''
            Delimitters
        '''
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACE', r'\{')
        self.lexer.add('CLOSE_BRACE', r'\}')

        '''
            Variables
        '''
        self.lexer.add('VARIABLE', r'\b[a-zA-Z_]\w*\b')

        '''
            Integer literals - Note we need to map INTEGER_FA to others
        '''
        self.lexer.add('INTEGER', r'\b\d+\b')

        '''
            Whitespace gets ignored
        '''
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

