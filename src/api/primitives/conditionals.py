class Conditional:
    def __init__(self, condition, true_branch, false_branch):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def evaluate(self, environment=None):
        if self.condition.evaluate() == True:
            return self.true_branch.evaluate()

        if self.false_branch == None:
            return None
        else:
            return self.false_branch.evaluate()

class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def evaluate(self, environment=None):
        while self.condition.evaluate():
            self.body.evaluate()