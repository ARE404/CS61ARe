from math import sqrt
from operator import add
from functools import reduce
def sum_naturals(n):
    return reduce(add,range(n,0,-1))
def sum_cubes(n):
    total=0
    for i in range(n,0,-1):
        total+=i*i*i
    return total
"""
def g(n,k,j):
    return reduce(k,j(range(n,0,-1)))
"""
def cube(x):
    return x*x*x
def p(x):
    return 8/((4*k-3)*(4*k-1))
def adapt(k,n):
    total=0
    for i in range(n,0,-1):
        total+=k(i)
    return total
def adaptive_cubes(x):
    return adapt(cube,x)
def identify(x):
    return x

def improve(update,close,guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def golden_update(guess):
    return 1/guess+1

def approx_close(x,y,tolerance=1e-3):
    return abs(x-y) < tolerance

def square_close_to_successor(guess):
    if approx_close(guess*guess,guess+1):
        return True
    else:
        return False

phi=improve(golden_update,square_close_to_successor)

def compose(f,g):
    def h(x):
        return f(g(x))
    return h

def addx(x):
    def g(y):
        return x+y
    return g

def print404():
    print("404")

testlambda=lambda x: print404()
