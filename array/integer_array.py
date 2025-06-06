
# 1. print the values of an array ?    O(n)
def values_of_an_array(my_list: list) -> None:
    # for nums in my_list:
    print(*my_list)

# 2. find the sum of all the numbers of an array ?   O(n)
def sum_of_an_array(my_array: list[int]) -> int:

    total = 0
    for nums in my_array:
        total += nums
    return total

# 3. find the maximum value of an array ?   TC- O(n), SC- O(1)
def maximum_value_of_an_array(my_array: list[int]) -> int:
    maximum = float("-inf")
    for i in my_array:
        if i > maximum:
            maximum = i
    return maximum

# 4. find the minimum number of an array ?   O(n)
def minimum_value_of_an_array(my_array: list[int]) -> int:
    minimum = float("inf")
    for i in my_array:
        if i < minimum:
            minimum = i
    return minimum

# 5. search for a tatget value ?   O(n)
def search_target(my_array: list[int], target: int) -> int:

    for i in my_array:
        if i == target:
            return target

# Reverse an array...
def reverseAnArray(x: list[int]):

    # Brute force
    

    # Two pointer
    i=0
    j=len(x)-1
    while i<=j:
        x[i], x[j] = x[j], x[i]

        i+=1
        j-=1
    
    return x



if __name__ == "__main__":
    array = [4,5,6,2,3]
    print(f"1st answer: {values_of_an_array(array)}")
    print(f"2nd answer: {sum_of_an_array(array)}")
    print(f"3rd answer: {maximum_value_of_an_array(array)}")
    print(f"4rth answer: {minimum_value_of_an_array(array)}")
    print(f"5th answer: {search_target(array, target=array[1])}")
    print(reverseAnArray([1,2,3,4,5]))