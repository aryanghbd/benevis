class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}

    def get(self, name):
        if name in self.variables:
            return self.variables[name]
        elif self.parent is not None:
            return self.parent.get(name)
        else:
            raise NameError(f"Variable '{name}' is not defined")

    def set(self, name, value):
        self.variables[name] = value

class Variable:
    def __init__(self, name):
        self.name = name

    def evaluate(self, environment=None):
        return environment.get(self.name)


class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def evaluate(self, environment):
        value = self.expression.evaluate(environment)
        environment.set(self.name.getstr(), value)
        return value