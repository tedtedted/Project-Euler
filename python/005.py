"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divisble_by_num(number):
	for i in range(3, 21):
		if number % i != 0:
			return False
	return True


# Increment by 20, given Blank Editor's advice here:
# https://www.youtube.com/watch?v=Km36RkQToqo
i = 20
while True:
	if divisble_by_num(i):
		print(i)
		break
	else:
		i += 20