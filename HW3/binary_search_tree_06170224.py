#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
#參考資料:https://www.youtube.com/watch?v=YlgPi75hIBc&feature=youtu.be影片裡面的概念以及之前程式碼學習的累積
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):#參考影片的概念並修改成全包在一個class的版本
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if val:
            if root.val:
                if root.val >= val:
                    if root.left:
                        return Solution().insert(root.left, val)
                    else:
                        root.left = TreeNode(val)
                        return root.left
                
                else:
                    if root.right:
                        return Solution().insert(root.right, val)
                    else:
                        root.right = TreeNode(val)
                        return root.right
                    
            else:
                root.val = val
                return root
            
    def delete(self, root, target):#根據search的概念去做調整
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if root.val == target:
            root.val = None
            if root.left:
                Solution().delete(root.left, target)
        elif root.val > target:
            if root.left:
                Solution().delete(root.left, target)
        else:
            if root.right:
                Solution().delete(root.right, target)
        
        if Solution().search(root, target) == None:
            new_root = TreeNode(None)
            Solution().rebuild(root, new_root)
            root = new_root
            return root
    def search(self, root, target):#參考影片並修改成全部包在一個class的版本
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root.val == target:
            return root
        else:
            if root.val == None:
                if root.left:
                    return Solution().search(root.left, target)
                elif root.right:
                    return Solution().search(root.right, target)
            elif root.val > target and root.left:
                return Solution().search(root.left, target)
            elif root.val < target and root.right:
                return Solution().search(root.right, target)
            else:
                return None
            
    def modify(self, root, target, new_val):#根據search的概念去做修正
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if root.val == target:
            root.val = new_val
            if root.left:
                Solution().modify(root.left, target, new_val)
        elif root.val > target:
            if root.left:
                Solution().modify(root.left, target, new_val)
        else:
            if root.right:
                Solution().modify(root.right, target, new_val)
                
        if Solution().search(root, target) == None:
            new_root = TreeNode(None)
            Solution().rebuild(root, new_root)
            root = new_root
            return root
    def rebuild(self, root, new_root):#參考影片中preorder的程式碼，並修改成這個版本
        if root:
            Solution().insert(new_root, root.val)
            if root.left:
                Solution().rebuild(root.left, new_root)
            if root.right:
                Solution().rebuild(root.right, new_root)


# In[ ]:




