#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Solution(object):
    def merge_sort(self, nums):
        left = []
        right = []
        if len(nums)<=1:
            return nums
        else:
            for i in nums[0:len(nums)//2]:
                left.append(i)
            for j in nums[len(nums)//2:]:
                right.append(j)
            left = merge_sort(left)
            right = merge_sort(right)
        
        return Merge(left,right)
    
    def Merge(left,right):
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


    

    
    


# In[29]:


output = Solution().merge_sort([5,3,78,5,64,2,6,9,34])
output


# In[ ]:





# In[ ]:





# In[ ]:




