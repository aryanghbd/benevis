class Program:
    def __init__(self, statements):
        self.statements = statements

    def evaluate(self, environment=None):
        for statement in self.statements:
            statement.evaluate(environment)
