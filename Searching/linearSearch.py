
# search for a target ?
def searchTarget(x: list[int], target: int):

    for i in x:
        if x[i]==target:
            return i
        

# Reverse an array
def reverseArray(arr: list[int]) -> list[int]:

    start=0
    end=len(arr)-1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start+=1
        end-=1

    return arr


# find single-unique number ?
def uniqueNum(arr: list[int]) -> int:

    for i in arr:
        value_count = arr.count(i)

        if value_count%2 != 0:
            print(i)





if __name__ == "__main__":
    # print(f"Index no. is: {searchTarget([4,6,2,3,8,1,9], 8)}")
    # print(reverseArray([1,2,3,4,5]))
    print(uniqueNum([4,1,2,1,2,5]))