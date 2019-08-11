# Lambda syntax:
# lambda <parameters>: <expression>
# See the docs:
# https://docs.python.org/3/reference/expressions.html#lambda


# Lambdas can be stored in a variable and invoked later
# No arguments
the_lambda = lambda: 42
the_lambda()

# One argument
the_lambda = lambda x: x
the_lambda(42)

# Two arguments
the_lambda = lambda x, y: x + y
the_lambda(41, 1)


# Lambdas can be passed directly to a function
# No arguments
def accepts_lambda(function_object):
    return function_object()

accepts_lambda(lambda: 42)

# One argument
def accepts_lambda(function_object):
    return function_object(42)

accepts_lambda(lambda x: x)

# Two arguments
def accepts_lambda(function_object):
    return function_object(41, 1)

accepts_lambda(lambda x, y: x + y)
