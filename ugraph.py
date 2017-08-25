import unittest as ut
from abc import ABCMeta,abstractmethod

class Graph:
    __metaclass__=ABCMeta
    
    @abstractmethod
    def insertEdge(self,e):
        pass

    @abstractmethod
    def removeEdge(self,e):
        pass

    @abstractmethod
    def dfsR(self,e):
        pass

class GraphInMatrix(Graph):
    edges=None
    def __init__(self,v):
        self.edges=[[0 for i in range(v)] for j in range(v)]

    def hasEdge(self,e):
        return self.edges[e.u][e.v]==1

    def insertEdge(self,e):
        self.edges[e.u][e.v]=self.edges[e.v][e.u]=1

    def removeEdge(self,e):
        self.edges[e.u][e.v]=self.edges[e.v][e.u]=0

    def dfsR(self,e):
        p= []

        return p

class GraphInList(Graph):
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

    vset=None
    path=None
    def hasPath(self,e):
        return self.getPath(e).count()>0

    def findPath(self,e):
        self.vset[e.u]=e.u
        self.path.append(e.u)
        if e.v in self.edges[e.u]:
            self.path.append(e.v)
            return True
        for v in self.edges[e.u]:
            if v not in self.vset and self.findPath(Edge(v,e.v)):
                return True
        self.path=self.path[0:-1]
        return False

    
    def getPath(self,e):
        self.path=[]
        self.vset={}
        self.findPath(e)
        return self.path


    def dfs(self):
        self.pre=[-1 for i in range(self.nodes)]
        self.st=[-1 for i in range(self.nodes)]
        self.cc=[-1 for i in range(self.nodes)]
        self.etypes={}
        self.cnt=-1
        self.c_i=-1
        for i in range(self.nodes):
            if self.pre[i]==-1:
                self.c_i+=1
                self.dfsR(Edge(i,i))

    def dfsR(self,e):
        if self.pre[e.v]==-1:
            self.cnt+=1
            self.pre[e.v]=self.cnt
            self.st[e.v]=e.u
            self.cc[e.v]=self.c_i
            self.etypes[e]='tree'
            for v in self.edges[e.v]:
                self.dfsR(Edge(e.v,v))
        else:
            if e.u == self.st[e.v]:
                self.etypes[e]='parent'
            else:
                if self.pre[e.u] > self.pre[e.v]:
                    self.etypes[e]='back'
                else:
                    self.etypes[e]='down'

    def hasCircle(self):
        for e in self.etypes:
            if self.etypes[e]=='back' or self.etypes[e]=='down':
                return True
        return False

    def connected(self,e):
        return self.cc[e.u]==self.cc[e.v]

    def bfs(self):
        self.pre=[-1 for i in range(self.nodes)]
        self.li=[]
        self.cnt=-1
        for i in range(self.nodes):
            if self.pre[i]==-1:
                self.li.append(Edge(i,i))
                while len(self.li)>0:
                    e=self.li.pop(0)
                    if self.pre[e.v] == -1:
                        self.cnt+=1
                        self.pre[e.v]=self.cnt
                        for v in self.edges[e.v]:
                            if self.pre[v]==-1:
                                self.li.append(Edge(e.v,v))



class Edge:
    u=0
    v=0
    w=1

    def __init__(self,u,v,w=1):
        self.u=u
        self.v=v
        self.w=w

class Test(ut.TestCase):

    def testDfs(self):
        g=GraphInList(8)
        g.insertEdges([Edge(0,7),Edge(0,5),Edge(0,2),
                       Edge(1,7),
                       Edge(2,0),Edge(2,6),
                       Edge(3,5),Edge(3,4),
                       Edge(4,6),Edge(4,5),Edge(4,7),Edge(4,3),
                       Edge(5,0),Edge(5,4),Edge(5,3),
                       Edge(6,4),Edge(6,2),
                       Edge(7,1),Edge(7,0),Edge(7,4)
                       ])
        g.dfs()
        self.assertEqual([0,2,5,7,3,6,4,1],g.pre)
        self.assertTrue(g.hasCircle())

    def testBfs(self):
        g=GraphInList(8)
        g.insertEdges([Edge(0,2),Edge(0,5),Edge(0,7),
                       Edge(1,7),
                       Edge(2,0),Edge(2,6),
                       Edge(3,5),
                       Edge(4,5),
                       Edge(5,0),Edge(5,3),Edge(5,4),
                       Edge(6,2),
                       Edge(7,0),Edge(7,1),
                       ])
        g.bfs()
        self.assertEqual([0,7,1,5,6,2,4,3],g.pre)

if __name__ == '__main__':
    ut.main()