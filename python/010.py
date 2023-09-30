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

NUM = 10
num_list = []

for i in range(1, NUM):

	if prime_number(i):
		print(i)