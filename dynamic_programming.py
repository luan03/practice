'''
Fibonacci: 1, 2, 3, 5, 8, 13, 21, 34 ...
F(1) = F(2) = 1
F(n) = F(n -1) + F(n - 2)
F(3) = F(2) + F(1) = 1 + 1 = 2
F(4) = F(3) + F(2) = 2 + 1 = 3

Fibonnaci is implemented using recursive function in both cases to present a 
clear solution. However, the first function is not optimized due to too many 
recalculations that have been made in the recursive approach. To avoid this 
negative effect was implemented dynamic programming in the second solution.

Dynamic Programming

Dynamic Programming is a technique for solving problems with overlapping 
subproblems. Each sub-problem is solved only once and the result of each 
sub-problem is stored in a table (generally implemented as an array or a 
hash table) for future references. These sub-solutions may be used to obtain 
the original solution and the technique of storing the sub-problem solutions 
is known as memoization.

In computing, memoization is an optimization technique used primarily to speed
up computer programs by storing the results of expensive function calls and 
returning the cached result when the same inputs occur again.

The main approach is solving optimization problem
'''

# 1. slow version
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 2. fast version
def fib_optimized(n):
    if n == 1 or n == 2:
        return 1
    
    f1 = 1
    f2 = 1
    
    for i in range(3, n + 1):
        f = f1 + f2
        f2 = f1
        f1 = f
    return f1
    
print('slow fib running')
print(fib(34))

print('fast fib running')
print(fib_optimized(34))