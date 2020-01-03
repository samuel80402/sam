#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        self.graph.append(w)
        self.graph_matrix[u][v]=w
        return self.graph.sort() 

    def Dijkstra(self, s):
        w = [0]*self.V#最後的花費
        t = [s]#走訪的順序
        index = []
        near = []
        answer = {}
        node = [i for i in range(self.V)]
        while len(t) != self.V:
            for i in range(self.V):
                if i not in t:#為了不算已經走過的，所以使用這個去擋
                    if w[i] == 0:#目前到哪都去不了，花費為0
                        if self.graph[t[-1]][i]!=0:
                            w[i] = self.graph[t[-1]][i] + w[t[-1]]#因為除了自己以外要加自己到起點的花費
                    else:
                        if w[i] > self.graph[t[-1]][i] + w[t[-1]] and self.graph[t[-1]][i] != 0:
                            w[i] = self.graph[t[-1]][i] + w[t[-1]]    
            for i in range(len(w)):
                if w[i] != 0 and i not in t:
                    index.append(i)
                    near.append(w[i])
            
            t.append(index[near.index(min(near))])
            index = []
            near = []
        for i in node:
            answer[str(i)] = w[i]
        return answer 

    def Kruskal(self):
        root = [-1]*self.V
        target = 0
        answer = []
        while target < len(self.graph):
            for i in range(self.V):
                for j in range(self.V):
                    if self.graph_matrix[i][j] == self.graph[target]:#target是花費的index，ij則是兩個相連的點
                        if root[j] == -1:
                            root[i],root[j] = i,i
                            w = print(str(i),"-",str(j))#這邊嘗試用奇怪的做法改成助教要的，但沒成功
                            answer.append(a)
                        elif root[i] == -1 != root[j] or root[i] != -1 != root:
                            for k in root:
                                if k == root[j]:
                                    k = i
                            w = print(str(i),"-",str(j))
                            answer.append(a)
            target+=1
        return root
#參考資料:https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p
#https://www.runoob.com/python/python-dictionary.html

