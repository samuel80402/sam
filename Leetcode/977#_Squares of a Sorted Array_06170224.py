#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Solution:
    def sortedSquares(self, A):
        answer = []
        for i in A:
            answer.append(i**2)
        answer.sort()
        return answer

