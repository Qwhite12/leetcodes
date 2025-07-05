""" 
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        lucky = -1
        for x in arr:
            if x == arr.count(x):
                lucky = x
        return lucky
