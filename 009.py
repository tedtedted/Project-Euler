"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def correct_triplet(a, b, c):

	return a + b + c == 1000


for i in range(1,1000):

	for j in range(1,1000):

		for k in range(1,1000):

			if i**2 + j**2 == k**2:
				if correct_triplet(i, j , k):
					print(i, j, k, i*j*k)