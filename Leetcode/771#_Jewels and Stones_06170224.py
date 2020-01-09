#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        n=0
        j = list(J)
        s = list(S)
        for i in s:
            if i in j:
                n+=1
        return n

