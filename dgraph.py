import unittest as ut
from abc import ABCMeta,abstractmethod


class Edge(object):
    def __init__(self,u,v,w=1):
        self.u=u
        self.v=v
        self.w=w
    def __hash__(self):
        return hash(str(self.u)+','+str(self.v))
    def __eq__(self,other):
        return self.u==other.u and self.v==other.v

class GraphInList():
    def __init__(self,v):
        self.edges=[[] for j in range(v)]
        self.nodes=v

    def hasEdge(self,e):
        return e.v in self.edges[e.u]

    def insertEdge2(self,e):
        self.edges[e.u].append(e.v)
        self.edges[e.v].append(e.u)

    def insertEdge(self,e):
        self.edges[e.u].append(e.v)

    def insertEdges(self,edges):
        for e in edges:
            self.insertEdge(e)

    def removeEdge(self,e):
        self.edges[e.u].remove(e.v)
        self.edges[e.v].remove(e.u)
    
    def getPath(self,e):
        self.path=[]
        self.vset={}
        self.findPath(e)
        return self.path


    def dfs(self):
        self.prev=[-1 for i in range(self.nodes)]
        self.post=[-1 for i in range(self.nodes)]
        self.st=[-1 for i in range(self.nodes)]
        self.cc=[-1 for i in range(self.nodes)]
        self.etypes={}
        self.prevCnt=-1
        self.postCnt=-1
        self.c_i=-1
        for i in range(self.nodes):
            if self.prev[i]==-1:
                self.c_i+=1
                self.dfsR(Edge(i,i))

    def dfsR(self,e):
        self.prevCnt+=1
        self.prev[e.v]=self.prevCnt
        self.st[e.v]=e.u
        self.cc[e.v]=self.c_i
        self.etypes[e]='tree'
        for v in self.edges[e.v]:
            if self.prev[v] == -1:
                self.dfsR(Edge(e.v,v))
            else:
                if self.post[v]==-1:
                    self.etypes[Edge(e.v,v)]='back'
                elif self.prev[e.v] < self.prev[v]:
                    self.etypes[Edge(e.v,v)]='down'
                else:
                    self.etypes[Edge(e.v,v)]='cross'
                
        self.postCnt+=1
        self.post[e.v]=self.postCnt
        

    def hasCircle(self):
        for e in self.etypes:
            if self.etypes[e]=='back':
                return True
        return False

    def connected(self,e):
        return self.cc[e.u]==self.cc[e.v]

    def bfs(self):
        self.prev=[-1 for i in range(self.nodes)]
        self.li=[]
        self.prevCnt=-1
        for i in range(self.nodes):
            if self.prev[i]==-1:
                self.li.append(Edge(i,i))
                while len(self.li)>0:
                    e=self.li.pop(0)
                    if self.prev[e.v] == -1:
                        self.prevCnt+=1
                        self.prev[e.v]=self.prevCnt
                        for v in self.edges[e.v]:
                            if self.prev[v]==-1:
                                self.li.append(Edge(e.v,v))



class Test(ut.TestCase):

    def testDfs(self):
        g=GraphInList(13)
        g.insertEdges([Edge(0,5),Edge(0,1),Edge(0,6),
                       Edge(3,2),
                       Edge(4,3),Edge(4,11),Edge(4,2),
                       Edge(5,4),
                       Edge(6,9),Edge(6,4),
                       Edge(7,8),Edge(7,6),
                       Edge(8,9),
                       Edge(9,10),
                       Edge(11,12),
                       Edge(12,9),
                       ])
        g.dfs()
        self.assertEqual([0,9,4,3,2,1,10,11,12,7,8,5,6],g.prev)
        self.assertEqual([10,8,0,1,6,7,9,12,11,3,2,5,4],g.post)
        self.assertEqual('down',g.etypes[Edge(4,2)])
        self.assertEqual('cross',g.etypes[Edge(7,6)])
        # self.assertTrue(g.hasCircle())

    # def testBfs(self):
    #     g=GraphInList(8)
    #     g.insertEdges([Edge(0,2),Edge(0,5),Edge(0,7),
    #                    Edge(1,7),
    #                    Edge(2,0),Edge(2,6),
    #                    Edge(3,5),
    #                    Edge(4,5),
    #                    Edge(5,0),Edge(5,3),Edge(5,4),
    #                    Edge(6,2),
    #                    Edge(7,0),Edge(7,1),
    #                    ])
    #     g.bfs()
    #     self.assertEqual([0,7,1,5,6,2,4,3],g.prev)

if __name__ == '__main__':
    ut.main()