#  Master control flow (if/else statements, for/while loops). Practice writing simple scripts.

from typing import List, Dict

# 1. Write a script that checks if a number is even or odd and prints the result.
def check_even_odd(number: int) -> None:
    """Checks if a number is even or odd and prints the result."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# 2. Write a script that prints the first 10 Fibonacci numbers.
def print_fibonacci() -> None:
    """Prints the first 10 Fibonacci numbers."""
    fib_sequence = [0, 1]
    while len(fib_sequence) < 10:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    print("First 10 Fibonacci numbers:", fib_sequence)

# 3. Write a script that calculates and prints the factorial of a given number.
def calculate_factorial(factorial_number: int) -> None:
    """Calculates and prints the factorial of a given number."""
    factorial = 1
    for i in range(1, factorial_number + 1):
        factorial *= i
    print(f"Factorial of {factorial_number} is {factorial}.")

# 4. Write a script that iterates through a list of numbers and prints only the prime numbers.
def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_list(numbers: List[int]) -> None:
    """Iterates through a list of numbers and prints only the prime numbers."""
    prime_numbers = [num for num in numbers if is_prime(num)]
    print("Prime numbers in the list:", prime_numbers)

# 5. Write a script that uses nested loops to print a multiplication table (1 to 10).
def print_multiplication_table() -> None:
    """Uses nested loops to print a multiplication table (1 to 10)."""
    print("Multiplication Table (1 to 10):")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i * j:4}", end=' ')
        print()

# 6. Write a script that checks if a given year is a leap year.
def check_leap_year(year: int) -> None:
    """Checks if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# 7. Write a script that sums all the numbers in a list using a for loop.
def sum_list(numbers_to_sum: List[int]) -> None:
    """Sums all the numbers in a list using a for loop."""
    sum_result = 0
    for num in numbers_to_sum:
        sum_result += num
    print(f"Sum of numbers in the list: {sum_result}")

# 8. Write a script that prints the multiplication table of a given number using a for loop.
def print_multiplication_table_for_number(multiplication_number: int) -> None:
    """Prints the multiplication table of a given number using a for loop."""
    print(f"Multiplication table of {multiplication_number}:")
    for i in range(1, 11):
        print(f"{multiplication_number} x {i} = {multiplication_number * i}")

# 9. Write a script that finds the largest number in a list using a for loop.
def find_largest_number(numbers_list: List[int]) -> None:
    """Finds the largest number in a list using a for loop."""
    if not numbers_list:
        return
    largest_number = numbers_list[0]
    for num in numbers_list:
        if num > largest_number:
            largest_number = num
    print(f"The largest number in the list is: {largest_number}")

# 10. Write a script that prints the first 20 numbers of the Fibonacci sequence using a while loop.
def print_fibonacci_20() -> None:
    """Prints the first 20 numbers of the Fibonacci sequence using a while loop."""
    fib_sequence_20 = [0, 1]
    while len(fib_sequence_20) < 20:
        next_number = fib_sequence_20[-1] + fib_sequence_20[-2]
        fib_sequence_20.append(next_number)
    print("First 20 Fibonacci numbers:", fib_sequence_20)

# 11. Write a script that checks if a string is a palindrome (reads the same forwards and backwards).
def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def check_palindrome(word: str) -> None:
    """Checks if a string is a palindrome (reads the same forwards and backwards) and prints result."""
    if is_palindrome(word):
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')

# 12. Write a script that prints the multiplication table of numbers from 1 to 10 using nested loops.
def print_multiplication_tables_1_to_10() -> None:
    """Prints the multiplication table of numbers from 1 to 10 using nested loops."""
    print("Multiplication Table (1 to 10) using nested loops:")
    for i in range(1, 11):
        print(f"Multiplication table of {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

# 13. Write a script that counts the number of vowels in a given string.
def count_vowels(s: str) -> int:
    """Counts the number of vowels in a given string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def print_vowel_count(text: str) -> None:
    """Counts the number of vowels in a given string and prints result."""
    vowel_count = count_vowels(text)
    print(f"Number of vowels in the text: {vowel_count}")

# 14. Write a script that prints the first 15 prime numbers using a while loop.
def print_first_15_primes() -> None:
    """Prints the first 15 prime numbers using a while loop."""
    prime_numbers_15 = []
    num = 2  # Starting number to check for primality
    while len(prime_numbers_15) < 15:
        if is_prime(num):
            prime_numbers_15.append(num)
        num += 1
    print("First 15 prime numbers:", prime_numbers_15)

# 15. Write a script that checks if a given number is a perfect number (equal to the sum of its proper divisors).
def is_perfect_number(n: int) -> bool:
    """Checks if a given number is a perfect number."""
    if n <= 0:
        return False
    divisors_sum = 1  # 1 is a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return n == divisors_sum

def check_perfect_number(perfect_number: int) -> None:
    """Checks if a given number is a perfect number and prints result."""
    if is_perfect_number(perfect_number):
        print(f"{perfect_number} is a perfect number.")
    else:
        print(f"{perfect_number} is not a perfect number.")

# 16. Write a script that prints the multiplication table of a given number in reverse order using a for loop.
def print_multiplication_table_reverse(reverse_multiplication_number: int) -> None:
    """Prints the multiplication table of a given number in reverse order using a for loop."""
    print(f"Multiplication table of {reverse_multiplication_number} in reverse order:")
    for i in range(10, 0, -1):
        print(f"{reverse_multiplication_number} x {i} = {reverse_multiplication_number * i}")

# 17. Write a script that finds the smallest number in a list using a for loop.
def find_smallest_number(numbers_list_smallest: List[int]) -> None:
    """Finds the smallest number in a list using a for loop."""
    if not numbers_list_smallest:
        return
    smallest_number = numbers_list_smallest[0]
    for num in numbers_list_smallest:
        if num < smallest_number:
            smallest_number = num
    print(f"The smallest number in the list is: {smallest_number}")

# 18. Write a script that prints the first 30 numbers of the Fibonacci sequence using a while loop.
def print_fibonacci_30() -> None:
    """Prints the first 30 numbers of the Fibonacci sequence using a while loop."""
    fib_sequence_30 = [0, 1]
    while len(fib_sequence_30) < 30:
        next_number = fib_sequence_30[-1] + fib_sequence_30[-2]
        fib_sequence_30.append(next_number)
    print("First 30 Fibonacci numbers:", fib_sequence_30)

# 19. Write a script that checks if a string is an anagram of another string.
def are_anagrams(str1: str, str2: str) -> bool:
    """Checks if a string is an anagram of another string."""
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

def check_anagrams(word1: str, word2: str) -> None:
    """Checks if a string is an anagram of another string and prints result."""
    if are_anagrams(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams.')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams.')

# 20. Write a script that counts the frequency of each character in a given string.
def char_frequency(s: str) -> Dict[str, int]:
    """Counts the frequency of each character in a given string."""
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def print_char_frequency(text_frequency: str) -> None:
    """Counts the frequency of each character in a given string and prints result."""
    frequency_result = char_frequency(text_frequency)
    print("Character frequencies in the text:")
    for char, count in frequency_result.items():
        print(f"'{char}': {count}")

# 21. Write a script that prints the multiplication table of numbers from 1 to 1000 using nested loops.
def print_multiplication_tables_1_to_1000() -> None:
    """Prints the multiplication table of numbers from 1 to 1000 using nested loops."""
    print("Multiplication Table (1 to 1000) using nested loops:")
    for i in range(1, 1001):
        print(f"Multiplication table of {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()

def main() -> None:
    """Main function to execute all examples."""
    check_even_odd(42)
    print_fibonacci()
    calculate_factorial(5)
    print_primes_in_list([2, 3, 4, 5, 10, 13, 17, 20, 23, 29])
    print_multiplication_table()
    check_leap_year(2024)
    sum_list([1, 2, 3, 4, 5])
    print_multiplication_table_for_number(7)
    find_largest_number([3, 5, 2, 8, 14])
    print_fibonacci_20()
    check_palindrome("racecar")
    print_multiplication_tables_1_to_10()
    print_vowel_count("Hello, World!")
    print_first_15_primes()
    check_perfect_number(28)
    print_multiplication_table_reverse(5)
    find_smallest_number([3, 5, 2, 8, 14])
    print_fibonacci_30()
    check_anagrams("listen", "silent")
    print_char_frequency("Hello, World!")
    # print_multiplication_tables_1_to_1000() # Commented out to avoid too much output

if __name__ == "__main__":
    main()
