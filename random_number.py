

# Task 1

def count_numbers(numbers):
    count = 0
    for num in numbers:
        count += 1
    return count

def find_min_max(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    total = calculate_sum(numbers)
    count = count_numbers(numbers)
    average = total / count
    return average

with open("Random.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

num_count = count_numbers(numbers)
min_num, max_num = find_min_max(numbers)
total_sum = calculate_sum(numbers)
average = calculate_average(numbers)

print("Number of numbers in the file:", num_count)
print("Largest number:", max_num)
print("Smallest number:", min_num)
print("Sum of all numbers:", total_sum)
print("Average of all numbers:", average)


# Task 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    print("Prime numbers up to", n, ":", primes)

n = int(input("Enter an integer greater than 1: "))
display_primes(n)