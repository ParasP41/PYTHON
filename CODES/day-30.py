'''#recursion#'''

# def factorial(n):
#     if (n==0 or n==1):
#         return 1;
#     else:
#         return n * factorial(n-1);
# print(factorial(5));

'''quick quiz: Write a recursive function print fabonacci series up to n'''

# a=0;
# b=1;
# print(a,b,end=' ');
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ');

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence 
print(fibonacci(10))
