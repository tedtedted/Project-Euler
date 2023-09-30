"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
find_prime = 600851475143
primes = []


# Find all factors of the (sqrt of the) large number
def get_factors(number):
	factors = []
	i = 2
	while i < number ** .5:
		if number % i == 0:
			factors.append(i)
		i += 1
	return factors


# check if number is prime (contains no factors other than 1 and itself)
def prime_number(number):
	return len(get_factors(number)) == 0


# iterate through all factors and check if they're prime.
for i in get_factors(find_prime):
	if prime_number(i):
		primes.append(i)


# grab the largest [-1] => last index
print("largest prime:", primes[-1])