import random

""" Random Numbers """
class RandomNumbers():
"""This is randomnumber class"""
    def __init__():
        pass

    def rand_num(amount, minRange, maxRange):
        assert(amount >= 0), "Amount is less than 0"
        assert (minRange < maxRange), "minRange is bigger than maxRange"
        list_of_numbers = []

        for _ in range(amount):
            list_of_numbers.append(random.randint(minRange, maxRange))

        assert(len(list_of_numbers) == amount), "Expected amount is not equal to amount in result"
        assert(all(i >= minRange for i in list_of_numbers)), "Expected numbers higher or equal to minRange"

        return list_of_numbers

print(RandomNumbers.rand_num(3, 1, 10))
