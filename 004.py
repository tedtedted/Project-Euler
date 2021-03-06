"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of 
									two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


palindromes = []


def is_palindrome(num):
	string = str(num)
	first = string[:]
	last = string[::-1]
	return string[:] == string[::-1]

for i in range(100, 1000):
	for j in range(100, 1000):
			if is_palindrome(i * j):
				palindrome = i * j
				palindromes.append(palindrome)

print("The largest palindrome is:", sorted(palindromes)[-1])