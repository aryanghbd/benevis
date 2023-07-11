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
        self.lexer.add('AGAR', r'\bagar\b')
        self.lexer.add('AGAR', r'\bاگر\b')

        self.lexer.add('DAR_GHEYRE_IN_SOORAT', r'\bdar gheyre in soorat\b')
        self.lexer.add('DAR_GHEYRE_IN_SOORAT', r'\bدر غیر این صورت\b')

        self.lexer.add('BARAYE', r'\bbaraye\b')
        self.lexer.add('BARAYE', r'\bبرای\b')

        self.lexer.add('TA', r'\bta\b')
        self.lexer.add('TA', r'\bتا\b')


        '''
        Operators
            -Things like +, -, *, /
            -Note that we can use words or the actual symbols for these, so each one comes as a pair (treated the same in AST)
        '''
        self.lexer.add('EZAFE', r'\bezafe\b')
        self.lexer.add('EZAFE', r'\bافزودن\b')
        self.lexer.add('PLUS', r'\+')

        self.lexer.add('MENHAYE', r'\bmenhaye\b')
        self.lexer.add('MENHAYE', r'\bکم کردن\b')
        self.lexer.add('MINUS', r'\-')

        self.lexer.add('ZARBDARE', r'\bzarbdare\b')
        self.lexer.add('ZARBDARE', r'\bضرب کردن\b')
        self.lexer.add('MULTIPLY', r'\*')

        self.lexer.add('TAGHSIM_BAR', r'\btaghsim bar\b')
        self.lexer.add('TAGHSIM_BAR', r'\bتقسیم بر\b')
        self.lexer.add('DIVIDE', r'\\')

        self.lexer.add('MOSAVIYE', r'\bmosaviye\b')
        self.lexer.add('MOSAVIYE', r'\bمساوی است با\b')
        self.lexer.add('EQUAL', r'\=')

        self.lexer.add('MOSAVI_NIST_BA', r'\bmosavi nist ba\b')
        self.lexer.add('MOSAVI_NIST_BA', r'\bمساوی نیست با\b')
        self.lexer.add('NEQ', r'\!=')


        '''
            Variables
        '''
        self.lexer.add('VARIABLE', r'\b[a-zA-Z_]\w*\b')

        '''
            Integer literals
        '''
        self.lexer.add('INTEGER', r'\b\d+\b')

        '''
            Whitespace gets ignored
        '''
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

