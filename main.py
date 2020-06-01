''' 
This repository runs a set of calculations to collect data on the
time efficiency of some simple algorithms.

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

SIZE_OF_ARRAY = 10000
STEP = 100
CYCLES_TO_RUN = 2
FIELDNAMES = ['range', 'average_time']

# O(1)
def access_element(numbers):
    return numbers[-1]

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


def calculate_average_times(times):
    average_times = []
    for i in range(len(times[0])):
        total = 0
        for j in range(len(times)):
            total += times[j][i]['time']
        average = total / len(times)
        average_times.append(
            {FIELDNAMES[0]: times[0][i][FIELDNAMES[0]],\
                FIELDNAMES[1]: average})
    return average_times


def generate_runtime_data(algorithm_to_run, numbers):
    times = []
    for j in range(CYCLES_TO_RUN):
        new = []
        for i in range(1, SIZE_OF_ARRAY, STEP):
            values = numbers[0:i]
            start = time.time_ns()
            total = algorithm_to_run(values)
            stop = time.time_ns()
            new.append({'range': i, 'time': stop-start})
        times.append(new)
    times = calculate_average_times(times)
    return times


def save_to_csv(values, headers, filename):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(values)


def run_o_constant(numbers, filename):
    average_times = generate_runtime_data(access_element, numbers)
    save_to_csv(average_times, FIELDNAMES, filename)


def run_o_n(numbers, filename):
    average_times = generate_runtime_data(sum, numbers)
    save_to_csv(average_times, FIELDNAMES, filename)


def run_o_log_n(filename):
    numbers = [i for i in range(SIZE_OF_ARRAY)]
    average_times = generate_runtime_data(divide, numbers)
    save_to_csv(average_times, FIELDNAMES, filename)


def run_o_n_pow_two(numbers, filename):
    average_times = generate_runtime_data(nested_loops, numbers)
    save_to_csv(average_times, FIELDNAMES, filename)


if __name__ == '__main__':

    # Create list filled with random numbers
    numbers = []
    for i in range(SIZE_OF_ARRAY):
        numbers.append(random.randrange(1, SIZE_OF_ARRAY))

    run_o_constant(numbers, 'o_constant.csv')
    #run_o_n(numbers, 'o_n.csv')
    #run_o_log_n('o_log_n.csv')
    #run_o_n_pow_two(numbers, 'quadratic.csv')
