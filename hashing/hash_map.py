
"""anagrams
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order."""

from collections import Counter

def anagrams(s1: str, s2:str) -> bool:
    # return Counter(s1) == Counter(s2)
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        # if char not in count:
        #     count[char] = 0
        # count[char] += 1
    return count

"""
Hashmap

"""
def twoSum(nums: list[int], target: int) -> int:
# O(n) - more optimized ----- Hash-map
    hashmap={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return hashmap[complement], i
        
        hashmap[num]=i


"""
Write a function, most_frequent_char, that takes in a string as an argument. 

The function should return the most frequent character of the string. If there are ties, 

return the character that appears earlier in the string.

You can assume that the input string is non-empty.

most_frequent_char('bookeeper') -> e

"""

def most_frequent_char(s: str) -> str:
    freq = {}

    # Count frequencies
    for char in s:
        # freq[char] = freq.get(char, 0) + 1

        if char not in freq:
            freq[char]=0
        
        freq[char]+=1

    max_count = 0
    result_char = ''

    # Loop through string again to preserve first-appearance rule
    for char in s:
        if freq[char] > max_count:
            max_count = freq[char]
            result_char = char

    return result_char
    
    pass


"""
Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return 

a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

pair_sum([3, 2, 5, 4, 1], 8) ->0,2

"""
def pair_sum(x: list[int], target: int):

    hashmap={}
    for i, num in enumerate(x):
        complement=target-num
        if complement in hashmap:
            return hashmap[complement], i
        
        hashmap[num] = i


    pass


"""pair product
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

pair_product([3, 2, 5, 4, 1], 8"""


"""Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]"""


if __name__ == "__main__":
    # s1 = input("Give me first name: ")
    # s2 = input("Give me second name: ")

    # print(anagrams(s1, s2))
    # print(char_count(s1))
    # print(most_frequent_char("aabc"))
    print(pair_sum([1,5,2,8], 3))