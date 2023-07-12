class BinaryOperation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class Subtract(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class Multiply(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class Divide(BinaryOperation):
    def evaluate(self):
        divisor = self.right.evaluate()
        if divisor == 0:
            raise ValueError("نمی‌توان بر صفر تقسیم کرد")

        return self.left.evaluate() / divisor
