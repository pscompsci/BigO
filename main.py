''' 
This repository runs a set of calculations to collect data on the
time efficiency of some simple alorithms.

To minimuse the effect of noise and other variations, in most cases
the algorithms are run multiple times and the average times recorded.

WARNING: Running this program in full will result in a long running 
process. It is easier to comment out the calls in main
so that each algorithm is run on it's own, and then run the program
several times.
'''

import random
import time
import csv

SIZE_OF_ARRAY = 10000000
STEP = 100000
CYCLES_TO_RUN = 20

# O(1)


def access_element(numbers, index):
    return numbers[index]

# O(n)


def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# O(log n)


def divide(number):
    while number > 0:
        number /= 2
    return number

# O(n^2)


def nested_loops(numbers):
    products = []
    for i in numbers:
        for j in numbers:
            products.append(i*j)
    return products


def average_times(times):
    average_times = []
    for i in range(len(times[0])):
        total = 0
        for j in range(len(times)):
            total += times[j][i]['time']
        average = total / len(times)
        average_times.append(
            {'range': times[0][i]['range'], 'average_time': average})
    return average_times


def save_to_csv(values, headers, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(values)


def run_o_constant(numbers, filename):
    times = []
    for i in range(1, SIZE_OF_ARRAY, STEP):
        start = time.time_ns()
        number = access_element(numbers, i)
        stop = time.time_ns()
        times.append({'index': i, 'time': stop-start})
    save_to_csv(times, ['index', 'time'], filename)


def run_o_n(numbers, filename):
    times = []
    for j in range(CYCLES_TO_RUN):
        new = []
        for i in range(1, SIZE_OF_ARRAY, STEP):
            start = time.time_ns()
            total = sum(numbers[0:i])
            stop = time.time_ns()
            new.append({'range': i, 'time': stop-start})
        times.append(new)
    times = average_times(times)
    save_to_csv(times, ['range', 'average_time'], filename)


def run_o_log_n(filename):
    times = []
    for j in range(CYCLES_TO_RUN):
        new = []
        for i in range(1, SIZE_OF_ARRAY, STEP):
            start = time.time_ns()
            total = divide(i)
            stop = time.time_ns()
            new.append({'range': i, 'time': stop-start})
        times.append(new)
    times = average_times(times)
    save_to_csv(times, ['range', 'average_time'], filename)


def run_o_n_pow_two(numbers, filename):
    times = []
    for j in range(CYCLES_TO_RUN//4):
        new = []
        for i in range(1, SIZE_OF_ARRAY/1000, STEP/1000):
            start = time.time_ns()
            total = nested_loops(numbers[0:i])
            stop = time.time_ns()
            new.append({'range': i, 'time': stop-start})
        times.append(new)
    times = average_times(times)
    save_to_csv(times, ['range', 'average_time'], filename)


if __name__ == '__main__':

    # Create list filled with random numbers
    numbers = []
    for i in range(SIZE_OF_ARRAY):
        numbers.append(random.randrange(1, SIZE_OF_ARRAY))

    run_o_constant(numbers, 'o_constant.csv')
    run_o_n(numbers, 'o_n.csv')
    run_o_log_n('o_log_n.csv')
    run_o_n_pow_two(numbers, 'quadratic.csv')
