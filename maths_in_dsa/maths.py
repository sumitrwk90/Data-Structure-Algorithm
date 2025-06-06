
""" write a function, is_prime, takes number as an input/argument and return boolean as an output ? """

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False

    return True

"""Write a function, fizz_buzz, that takes in a number n as an argument. The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

if the number is divisible by 3, make the element "fizz"
if the number is divisible by 5, make the element "buzz"
if the number is divisible by 3 and 5, make the element "fizzbuzz"

 TC- O(n), SC- O(n)"""  

def fizz_buzz(number: int) -> list:
    result = []

    for i in range(1, number+1):
        
        if i%3==0 and i%5==0:
            result.append("fizzbuzz")
        elif i%3==0:
            result.append("fizz")
        elif i%5==0:
            result.append("buzz")
        else:
            result.append(i)

    return result
            
"""Write a function, pairs, that takes in a list as an argument. The function should return a list containing all unique pairs of elements.

You may return the pairs in any order and the order of elements within a single pair does not matter.

You can assume that the input list contains unique elements."""

def pairs(elements: list) -> list:

    result = []

    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            pair = [elements[i], elements[j]]
            result.append(pair)

    return result






if __name__ == "__main__":
    # num = int(input("Give me a number: "))
    ele = ["a", "b", "a"]
    # print(is_prime(num))
    # print(fizz_buzz(num))
    print(pairs(ele))