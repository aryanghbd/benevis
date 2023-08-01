class Print:
    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, environment=None):
        val = self.expr.evaluate(environment)
        print(val)