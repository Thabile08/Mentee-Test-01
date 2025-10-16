def add_numbers(a, b):
    """
    Problem 1:
    Write a function that takes two numbers (a and b)
    and returns their sum.

    Example:
    >>> add_numbers(2, 3)
    5
    """
    # TODO: Write your code below
    a = 2
    b = 3
    c = a + b
    return c
print(add_numbers(a = 2, b = 3))



def is_even(n):
    """
    Problem 2:
    Return True if the given number 'n' is even, otherwise return False.

    Example:
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    """
    # TODO: Write your code below
    if n % 2 == 0:
        return True
    else:
         return False

print(is_even(16))


def count_vowels(word):
    """
    Problem 3:
    Write a function that counts how many vowels are in a given string.

    Vowels are: a, e, i, o, u (both uppercase and lowercase).

    Example:
    >>> count_vowels("Hello")
    2
    """
    # TODO: Write your code below
    word = "Hello"

    count = 0
    for i in word:
        if count_vowels == word:
            i += 1
            return count

print(count_vowels("Hello"))


'''def find_max(numbers):
    """
    Problem 4:
    Given a list of numbers, return the largest number.

    Example:
    >>> find_max([1, 4, 2, 10])
    10
    """
    # TODO: Write your code below
    list = [1,4,2,10]

    for i in list:'''

    


def reverse_string(s):
    """
    Problem 5:
    Write a function that returns the reverse of the input string.

    Example:
    >>> reverse_string("cat")
    'tac'
    """
    # TODO: Write your code below
    a = 'cat'
    s = 'tac'
    sorted(s) == sorted(a)
    return "cat"



print(reverse_string('cat'))



    


def average(numbers):
    """
    Problem 6:
    Given a list of numbers, return their average.
    If the list is empty, return 0.

    Example:
    >>> average([2, 4, 6])
    4.0
    >>> average([])
    0
    """
    # TODO: Write your code below
    pass


def word_in_sentence(word, sentence):
    """
    Problem 7:
    Return True if the given word appears in the sentence, otherwise False.

    Example:
    >>> word_in_sentence("cat", "The cat is sleeping")
    True
    >>> word_in_sentence("dog", "The cat is sleeping")
    False
    """
    # TODO: Write your code below

    word_in_sentence = "The cat is sleeping"

    for i in word_in_sentence:
        if word in word_in_sentence == "cat":
            return True
        else:
            return False
        
print(word_in_sentence(word = "dog",sentence="The cat is sleeping"))





def factorial(n):
    """
    Problem 8:
    Write a function that returns the factorial of a non-negative integer n.
    The factorial of n (written as n!) is the product of all positive integers up to n.
    If n is 0, return 1.

    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    # TODO: Write your code below
    pass


def remove_duplicates(numbers):
    """
    Problem 9:
    Given a list of numbers, return a new list with duplicates removed.
    The order of the first occurrence of each element should be preserved.

    Example:
    >>> remove_duplicates([1, 2, 2, 3, 1])
    [1, 2, 3]
    """
    # TODO: Write your code below
    numbers = [1, 2, 2, 3, 1]
    new_list = []
    pass



def fizzbuzz(n):
    """
    Problem 10:
    Write a function that returns a list of numbers from 1 to n, 1
    but replace:
    - multiples of 3 with "Fizz"
    - multiples of 5 with "Buzz"
    - multiples of both 3 and 5 with "FizzBuzz"

    Example:
    >>> fizzbuzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    """
    # TODO: Write your code below
    list = []
    for i in range(1, int(n)):
        i = i + 1
        list.insert(3,'Fizz')
        list.insert(5,'Buzz')
        return list

print(fizzbuzz(24))
print(fizzbuzz(24))
