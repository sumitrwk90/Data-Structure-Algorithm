
"""print all subset
    
    {1,2,3} - {1}, {2}, {3}, {1, 2}, {2, 3}, {1, 3}, {1,2,3}, {}"""

def printSubset(arr: list[int], ans: list[int], i: int) -> None:

    if i == len(arr):
        print(ans)
        
        return;

    # include arr...
    ans.append(arr[i])
    printSubset(arr, ans, i+1)
    
    # exclude arr...
    ans.pop()
    printSubset(arr, ans, i+1)


# Print all subset whose sum is exactly equal to target...
def subsetSumTarget(arr: list[int], ans: list[int], i: int, currentSum: int, target: int):
    if i == len(arr):
        if currentSum == target:
            print(ans)
        return

    ans.append(arr[i])
    subsetSumTarget(arr, ans, i + 1, currentSum + arr[i], target)

    ans.pop()
    subsetSumTarget(arr, ans, i + 1, currentSum, target)


# Permutations of list...
def permutations(arr: list[int], ans: list[int], used: list[bool]):
    if len(ans) == len(arr):
        print(ans)
        return

    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            ans.append(arr[i])
            permutations(arr, ans, used)
            ans.pop()
            used[i] = False


# combination sum

def combinationSum(candidates: list[int], ans: list[list[int]], target: int) -> list[list[int]]:

    pass


# Print all subsets...

def getSubsets(arr: list[int], ans: list[int], i: int, allSubsets) -> list[list[int]]:
    if i == len(arr):
        allSubsets.append(ans)

        return

    # Include current element
    ans.append(arr[i])
    getSubsets(arr, ans, i + 1, allSubsets)

    # Exclude current element
    ans.pop()
    getSubsets(arr, ans, i + 1, allSubsets)



# Print all subsets...

def getSubsets(arr: list[int], ans: list[int], i: int) -> list[list[int]]:
    if i == len(arr):
        return [list(ans)]

    # Include current element
    ans.append(arr[i])
    left = getSubsets(arr, ans, i + 1)

    # Exclude current element
    ans.pop()
    right = getSubsets(arr, ans, i + 1)

    return left + right



if __name__ == "__main__":
    # print(f"print the list of all subsets:\n {getSubsets([1,2,3], [], 0)}")
    # print(f"print all the subsets:\n {printSubset([1,2,3], [], 0)}")
    # print(subset())
    # print(subsetSumTarget([1,2,3], [], 0, 0, 3))
    print(permutations([1,2,3], [], [False, False, False]))
