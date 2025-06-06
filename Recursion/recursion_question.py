
"""Write a function sum_numbers_recursive that takes in an array of numbers and returns the sum of all 

the numbers in the array. All elements will be integers. Solve this recursively.

sum_numbers_recursive([5, 2, 9, 10]); # -> 26"""

import numpy as np
def sum_numbers_recursive(my_array: list) -> int:

    if not my_array:
        return 0;

    return my_array[0] + sum_numbers_recursive(my_array[1:])


"""factorial"""

def factorial(n: int) -> int:
    if n==0:
        return 1;

    return n * factorial(n-1);


"""sum of length - take a list of string as input, return total sum of their length as output"""

def sum_of_length(arr):

    if not arr:
        return 0

    return len(arr[0]) + sum_of_length(arr[1:])


"""length of n integers of an arr
  arr = [4,5,6]
  len = 3"""

def length_of_arr(arr: list) -> int:

    if not arr:
        return 0;

    return 1 + length_of_arr(arr[1:])


"""sum of n numbers - 
   if n=5
      
      sum = n + (n-1) + (n-2) + (n-3) + (n-4) + until n gets zero..."""

def sum(n: int) -> int:

    if not n:
        return 0
    
    return n + sum(n-1)


"""reverse string recursive"""

def reverse(s: str) -> str:

    if len(s) <= 1:
        return s;

    return reverse(s[1:]) + s[0]


"""palindrom recursive"""

def palindrom(s: int): #-> bool:
    # # Recursion
    # if len(s) <= 1:
    #     return True;

    # return s[0] == s[-1] and palindrom(s[1:-1])

    # slicing
    x_str = str(s)

    return x_str == x_str[::-1]



"""fibonacci"""

def fib(n: int) -> int:

    if n==0 or n==1:
        return n
    
    return fib(n-1) + fib(n-2)


"""Check if sorted 'Ascending order' """

def isSorted(arr: list) -> bool:

    if len(arr) <= 1:
        return 1;

    # return arr[len(arr)-1] >= arr[len(arr)-2] and isSorted(arr[len(arr)-1])
    return arr[-1] >= arr[-2] and isSorted(arr[:-1])


"""Reverse an array"""




if __name__ == "__main__":
    array = [5,2,9,10]
    # print(sum_numbers_recursive([5,2,9,10]))
    # print(factorial(5))
    # # str_arr = ["dog", "cat", "elephant"]
    # print(sum_of_length(["dog", "cat", "elephant"]))
    # print(fib(8))
    # print(isSorted(array))
    # print(reverse("abcd"))
    print(palindrom("12341"))
    # print(reverseAnArray(array))