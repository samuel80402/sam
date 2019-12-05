#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5
#參考資料: 助教測資與https://github.com/imucici/my-learning-note/blob/master/HW3/binary_search_tree_06170211.py

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        if self.contains(key) == False:
            password = self.getpassword(key)
            i = password % self.capacity
            if self.data[i] == None:
                self.data[i] = ListNode(password)
            else:
                node = self.data[i]
                nodenext = node.next
                while nodenext != None:#這邊參考網址中以while去走訪的方式
                    node = nodenext
                    nodenext = node.next
                node.next = ListNode(password)
        
    def remove(self, key):
        password = self.getpassword(key)
        i = password % self.capacity
        if self.data[i].val == password:
            if self.data[i].next == None:
                self.data[i] = None
            else:
                self.data[i] = self.data[i].next
        else:
            if self.data[i].next:
                n = self.data[i]
                nnext = n.next
                while nnext and nnext.val != password:#這邊參考網址中以while去走訪的方式
                    n = nnext
                    nnext = n.next
                if nnext:
                    if nnext.next:
                        n.next = nnext.next
                    else:
                        n.next = None
                
        
            
    def contains(self, key):
        password = self.getpassword(key)
        i = password % self.capacity
        if self.data[i] == None:
            return False
        elif self.data[i].val == password:
            return True
        else:
            node = self.data[i]
            nextnode = node.next
            while nextnode:#這邊參考網址中以while去走訪的方式
                if nextnode.val == password:
                    return True
                else:
                    nextnode = nextnode.next
            if nextnode == None:
                return False
        
    def getpassword(self, key):#這邊參考助教提供的MD5加密方式
        h = MD5.new()
        h.update(key.encode("utf-8"))
        return int(h.hexdigest(), 16)

