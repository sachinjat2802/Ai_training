#  Master control flow (if/else statements, for/while loops). Practice writing simple scripts.

# 1. Write a script that checks if a number is even or odd and prints the result.
number = 42  # You can change this number to test with different values
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 2. Write a script that prints the first 10 Fibonacci numbers.
fib_sequence = [0, 1]
while len(fib_sequence) < 10:
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)
print("First 10 Fibonacci numbers:", fib_sequence)

# 3. Write a script that calculates and prints the factorial of a given number.
factorial_number = 5  # You can change this number to test with different values
factorial = 1
for i in range(1, factorial_number + 1):
    factorial *= i
print(f"Factorial of {factorial_number} is {factorial}.")

# 4. Write a script that iterates through a list of numbers and prints only the prime numbers.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29]
prime_numbers = [num for num in numbers if is_prime(num)]
print("Prime numbers in the list:", prime_numbers)

# 5. Write a script that uses nested loops to print a multiplication table (1 to 10).
print("Multiplication Table (1 to 10):")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=' ')
    print()

# 6. Write a script that checks if a given year is a leap year.
year = 2024  # You can change this year to test with different values
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 7. Write a script that sums all the numbers in a list using a for loop.
numbers_to_sum = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers_to_sum:
    sum_result += num
print(f"Sum of numbers in the list: {sum_result}")

# 8. Write a script that prints the multiplication table of a given number using a for loop.
multiplication_number = 7  # You can change this number to test with different values
print(f"Multiplication table of {multiplication_number}:")
for i in range(1, 11):
    print(f"{multiplication_number} x {i} = {multiplication_number * i}")

# 9. Write a script that finds the largest number in a list using a for loop.
numbers_list = [3, 5, 2, 8, 14]
largest_number = numbers_list[0]
for num in numbers_list:
    if num > largest_number:
        largest_number = num
print(f"The largest number in the list is: {largest_number}")

# 10. Write a script that prints the first 20 numbers of the Fibonacci sequence using a while loop.
fib_sequence_20 = [0, 1]
while len(fib_sequence_20) < 20:
    next_number = fib_sequence_20[-1] + fib_sequence_20[-2]
    fib_sequence_20.append(next_number)
print("First 20 Fibonacci numbers:", fib_sequence_20)

# 11. Write a script that checks if a string is a palindrome (reads the same forwards and backwards).
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

word = "racecar"  # You can change this word to test with different values
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')

# 12. Write a script that prints the multiplication table of numbers from 1 to 10 using nested loops.
print("Multiplication Table (1 to 10) using nested loops:")
for i in range(1, 11):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# 13. Write a script that counts the number of vowels in a given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = "Hello, World!"  # You can change this text to test with different values
vowel_count = count_vowels(text)
print(f"Number of vowels in the text: {vowel_count}")

# 14. Write a script that prints the first 15 prime numbers using a while loop.
prime_numbers_15 = []
num = 2  # Starting number to check for primality
while len(prime_numbers_15) < 15:
    if is_prime(num):
        prime_numbers_15.append(num)
    num += 1
print("First 15 prime numbers:", prime_numbers_15)

# 15. Write a script that checks if a given number is a perfect number (equal to the sum of its proper divisors).
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 1  # 1 is a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return n == divisors_sum

perfect_number = 28  # You can change this number to test with different values

if is_perfect_number(perfect_number):
    print(f"{perfect_number} is a perfect number.")
else:
    print(f"{perfect_number} is not a perfect number.")

# 16. Write a script that prints the multiplication table of a given number in reverse order using a for loop.
reverse_multiplication_number = 5  # You can change this number to test with different values
print(f"Multiplication table of {reverse_multiplication_number} in reverse order:")
for i in range(10, 0, -1):
    print(f"{reverse_multiplication_number} x {i} = {reverse_multiplication_number * i}")


# 17. Write a script that finds the smallest number in a list using a for loop.
numbers_list_smallest = [3, 5, 2, 8, 14]
smallest_number = numbers_list_smallest[0]
for num in numbers_list_smallest:
    if num < smallest_number:
        smallest_number = num
print(f"The smallest number in the list is: {smallest_number}")

# 18. Write a script that prints the first 30 numbers of the Fibonacci sequence using a while loop.
fib_sequence_30 = [0, 1]
while len(fib_sequence_30) < 30:
    next_number = fib_sequence_30[-1] + fib_sequence_30[-2]
    fib_sequence_30.append(next_number)
print("First 30 Fibonacci numbers:", fib_sequence_30)

# Note: The above scripts demonstrate various control flow constructs in Python.
# 19. Write a script that checks if a string is an anagram of another string.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')

# 20. Write a script that counts the frequency of each character in a given string.
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

text_frequency = "Hello, World!"  # You can change this text to test with different values
frequency_result = char_frequency(text_frequency)
print("Character frequencies in the text:")
for char, count in frequency_result.items():
    print(f"'{char}': {count}")


# 21. Write a script that prints the multiplication table of numbers from 1 to 1000 using nested loops.
print("Multiplication Table (1 to 1000) using nested loops:")
for i in range(1, 1001):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()




