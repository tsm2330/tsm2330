# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:37:00 2022

@author: user
"""

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        leftmin,rightmax=[0 for i in range (len(prices))],[0 for i in range (len(prices))]
        leftmin[0]=prices[0]
        for i in range(1,len(prices)):
            leftmin[i]=min(leftmin[i-1],prices[i])
        rightmax[-1]=prices[-1]
        for i in range (len(prices)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],prices[i])
        ans=0
        for i in range(len(prices)-1):
            ans=max(ans,rightmax[i+1-leftmin[i]])
        return ans
ob1=Solution()
print(ob1.maxProfit([7,2,5,8,6,3,1,4,5,4,7]))    
        
class Solution(object):
   def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      if not prices:
         return 0
      leftMin,rightMax = [0 for i in range(len(prices))],[0 for i in range(len(prices))]
      leftMin[0] = prices[0]
      for i in range(1,len(prices)):
         leftMin[i] = min(leftMin[i-1],prices[i])
      #print(leftMin)
      rightMax[-1]= prices[-1]
      for i in range(len(prices)-2,-1,-1):
         rightMax[i] = max(rightMax[i+1],prices[i])
      #print(rightMax)
      ans = 0
      for i in range(len(prices)-1):
         ans = max(ans,rightMax[i+1]-leftMin[i])
      return ans
ob1 = Solution()
print(ob1.maxProfit([7,2,5,8,6,3,1,4,5,4,7]))