#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict   

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        node = [s]
        queue = [] + self.graph[s]
        i=0
        while len(node) != len(self.graph):
            node.append(queue[i])
            i+=1
            for j in self.graph[node[i]]:
                if j not in queue and j not in node:
                    queue.append(j)
        return node
    def DFS(self, s):
        node = [s]
        stack = [] + self.graph[s]
        while len(node) != len(self.graph):
            node.append(stack.pop(-1))
            for i in self.graph[node[-1]]:
                if i not in stack and i not in node:
                    stack.append(i)
        return node
#參考資料
#[BFS]https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
#[DFS]https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
#[not in]https://blog.csdn.net/DeniuHe/article/details/77985505

