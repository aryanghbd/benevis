from compiler.primitives import integer, variable
import rply

env = variable.Scope()

# Create an assignment statement

variable_token = rply.Token('VARIABLE', 'x')
expression = integer.Integer(5)
assignment = variable.Assignment(variable_token, expression)

# Evaluate the assignment in the environment
result = assignment.evaluate(env)

# Print the result and check the environment
print(result)  # Output: 5
print(env.get('x'))  # Output: 5