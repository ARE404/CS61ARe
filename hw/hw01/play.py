def fib(x):
    """cauculate xth fibnacci number"""
    if x == 1:
        return 0
    if x == 2:
        return 1
    return  fib(x-1)+fib(x-2)

def fib_while(x):
    """use while statement to cauculate xth fib number"""
    total = 0
    pred, curr = 0, 1
    while x >= 2:
        pred, curr = curr, pred + curr
        total = curr
        x = x - 1
    return total

def fib_test():
    """test function fib"""
    assert fib(1)==0, 'The 1st Fibonacci number should be 0'
    assert fib(2)==1, 'The 2st Fibonacci number should be 1'
    assert fib(8)==13, 'The 8st Fibonacci number should be 13'

    assert fib_while(8)==13, 'The 8st Fibonacci number should be 13'

def wears_jacket(temp, raining):
    "*** YOUR CODE HERE ***"
    return if temp<60 or raining