class BinaryOperation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperation):
    def evaluate(self, environment=None):
        return self.left.evaluate(environment) + self.right.evaluate(environment)

class Subtract(BinaryOperation):
    def evaluate(self, environment=None):
        return self.left.evaluate(environment) - self.right.evaluate(environment)

class Multiply(BinaryOperation):
    def evaluate(self, environment=None):
        return self.left.evaluate(environment) * self.right.evaluate(environment)

class Divide(BinaryOperation):
    def evaluate(self, environment=None):
        divisor = self.right.evaluate(environment)
        if divisor == 0:
            raise ValueError("نمی‌توان بر صفر تقسیم کرد")

        return self.left.evaluate(environment) / divisor
