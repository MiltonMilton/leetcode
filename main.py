from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for primary_index, primary_number in enumerate(nums):
        for secondary_index, secondary_number in enumerate(nums[primary_index + 1:]):
            if primary_number + secondary_number == target:
                return [primary_index, 1 + primary_index + secondary_index]

if __name__ == '__main__':
    test_1 = twoSum([2,7,11,15],9) == [0,1]
    test_2 = twoSum([3,2,4],6) == [1,2]
    test_3 = twoSum([3,3], 6) == [0,1]
    print ("test_1", test_1)
    print ("test_2", test_2)
    print ("test_3", test_3)
