number = 100


def sum_of_squares(num):
	sums = []
	for i in range(1, num + 1):
		sums.append(i**2)
	return sum(sums)


def square_of_sums(num):
	sums = 0
	for i in range(1, num + 1):
		sums += i
	return sums ** 2


print("Difference between: {}".format(square_of_sums(number) - sum_of_squares(number)))