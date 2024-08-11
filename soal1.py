from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    number = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in number:
            return [number[complement], index]
        
        number[num] = index
    
    return []

# Contoh penggunaan
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
