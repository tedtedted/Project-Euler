"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fib(n):
 	a,b = 1,1
 	for i in range(n-1):
  		a,b = b,a+b
 	return a

def memoize(fn, arg):
 	memo = {}
 	if arg not in memo:
  		memo[arg] = fn(arg)
  		return memo[arg]


fib_list = [0]
i = 2

while fib_list[-1] < 4000000:
	fib_try = memoize(fib,i)
	if fib_try % 2 == 0:
		fib_list.append(fib_try)
	i += 1


fib_list.remove(fib_list[-1])
print(sum(fib_list))