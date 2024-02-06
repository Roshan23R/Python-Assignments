from functools import reduce
import math

def calculate_mean(data):
    return sum(data)/len(data)

def calculate_median(data):
    l = len(data)
    data.sort()
    return (data[(l)//2] if (l % 2 !=0) else (data[l//2 -1] + data[(l)//2])/2)

def cumulative_sum(data):
    result = []
    total = 0
    for value in data:
        total += value
        result.append(total)
    return result


def calculate_variance(data):
    return (calculate_mean([num ** 2 for num in data]) - calculate_mean(data)**2)

def calculate_std(data):
    return math.sqrt(calculate_variance(data))


    

