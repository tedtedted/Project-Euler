"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Find all factors of the (sqrt of the) large number
def get_factors(number):
	factors = []
	i = 2
	while i < number:
		if number % i == 0:
			factors.append(i)
		i += 1
	return factors


# check if number is prime (contains no factors other than 1 and itself)
def prime_number(number):
	return len(get_factors(number)) == 0

print("Running")
i = 2
prime_count = 0
while prime_count <= 10001:
	if prime_number(i):
		prime_count += 1
	if prime_count == 10001:
		print("the {}th prime is: {}".format(prime_count, i))
		break
	i += 1