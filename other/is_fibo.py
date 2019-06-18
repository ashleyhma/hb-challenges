def solve(n):
    """Display IsFibo if  is a Fibonacci number and IsNotFibo if it is not. The output for each test case should be displayed in a new line."""
    fib_nums = set()

    a=0
    b=1

    for i in range(10000):
        c=a+b
        fib_nums.add(c)
        a=b
        b=c
    
    if n in fib_nums:
        return "IsFibo"
    else:
        return "IsNotFibo"