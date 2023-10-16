"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""


def count_evens(readings):

    my_list = []

    even_count = 0
    even_sum = 0

    for num in readings:
        if num % 2 == 0:
            even_count += 1
            even_sum += num

    my_list.append(even_count)
    my_list.append(even_sum)
    return tuple(my_list)


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count_evens(sample_list))
