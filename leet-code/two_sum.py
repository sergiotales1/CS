from typing import List

def twoSum(nums: List[int], target: int) -> List[int]: # List is just a type we don't actually need it 
    print(f"Input array: {nums}, target: {target}")
    prevMap = {}  # value : index
    for i, n in enumerate(nums): # Enumerate gives us index and value for each item, for example: (0, 5) (1, 2) (2, 6)
        diff = target - n
        if diff in prevMap: # Check if we already have this key (index) in the hashMap
            print(prevMap)
            return [prevMap[diff], i]
        prevMap[n] = i
    return


def mv(arr, target):
    prevMap = {} # index ; value

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

nums = [2, 7, 4, 11, 15]
target = 15
# result = twoSum(nums, target)
result = mv(nums, target)
print(f"Result: {result}")















