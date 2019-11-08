#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Solution(object):
    def heap_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        n = len(nums)
        for i in range(n-1,-1,-1):
            heapify(nums,i,n)
        for i in range(n-1,0,-1):
            nums[i],nums[0] = nums[0],nums[i]
            heapify(nums,0,i)
        
        return nums    

    def heapify(nums,i,n):
        root = i
        left = i*2+1
        right = i*2+2
        if left < n and nums[left] > nums[root]:
            root = left
        if right < n and nums[right] > nums[root]:
            root = right
        if i != root:
            nums[i],nums[root] = nums[root],nums[i]
            heapify(nums,root,n)
        


# In[30]:


output = Solution().heap_sort([5,3,78,5,64,2,6,9,34])
output


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




