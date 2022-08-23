# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:00:49 2022

@author: user
"""


class Solution(object):
   def containsDuplicate(self, nums):
      """
      :type nums: List[int]
      :rtype: bool
      """
      return not len(nums) == len(set(nums))
ob1 = Solution()
print(ob1.containsDuplicate([1,5,6,2,1,3]))
print(ob1.containsDuplicate([1,2,3,4]))

class solution(object):
    def containsDuplicate(self,nums):
        return not len(nums) ==len(set(nums))
ob1=Solution()
print(ob1.containsDuplicate([1,5,6,2,1,3]))
print(ob1.containsDuplicate([1,2,3,4]))