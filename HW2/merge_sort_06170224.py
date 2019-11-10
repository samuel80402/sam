#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        left = []
        right = []
        if len(nums)<=1:
            return nums
        else:
            for i in nums[0:len(nums)//2]:
                left.append(i)
            for j in nums[len(nums)//2:]:
                right.append(j)
            left = Solution().merge_sort(left)
            right = Solution().merge_sort(right)
        
        return Solution().Merge(left,right)
    
    def Merge(self,left,right):
        m = []
        i = 0
        j = 0
        for k in range(len(left)+len(right)):
            if j == len(right):
                m = m+left[i:]
                break
            elif i == len(left):
                m = m+right[j:]
                break
            elif left[i]<=right[j]:
                m.append(left[i])
                i+=1
            elif left[i]>right[j]:
                m.append(right[j])
                j+=1

        return m


    

    
    

