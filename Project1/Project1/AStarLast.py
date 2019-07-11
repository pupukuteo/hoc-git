
import math
dc = [-1, 0, 1, 0]
dr = [0, -1, 0, 1]

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.f = 0
        self.parent = Node
    def h(self, target):
        return math.fabs(self.row - target[0]) + math.fabs(self.col - target[1])
        # return 3.14*3.14*((self.row - int((self.row+target[0])/2))*(self.row - int((self.row+target[0])/2)) + (self.col - int((self.col+target[1])/2))*(self.col - int((self.col+target[1])/2)))
        # return (self.row - target[0])*(self.row - target[0]) + (self.col - target[1])*(self.col - target[1])
class AStar:
    def __init__(self, n):
        self.size = n
        m = []
        for indexX in range(0, n):
            tmp = []
            for indexY in range(0, n):
                tmp.append(0)
            m.append(tmp)
        # for index in range(0, 100):
        #     row = random.randrange(0, n)
        #     col = random.randrange(0, n)
        #     if((row == 0 and col == 0) or (row == n-1 and col == n-1)):
        #         continue
        #     m[row][col] = -1
        self.map = m
    def getMinF(self, ls):
        self.minF = 100000000
        idx = -1
        for i in range(0, len(ls)):
            if(ls[i].f < self.minF):
                self.minF = ls[i].f
                idx = i
        return idx
    def findNode(self, ps, ls):
        for i in range (0, len(ls)):
            if(ls[i].row == ps[0] and ls[i].col == ps[1]):
                return i
        return -1
    def solve(self, src, trg):
        OPEN = []
        CLOSE = []
        nSource = Node(src[0], src[1])
        # Set f(S) = h(S)
        nSource.g = 0
        nSource.f = nSource.h(trg)
        # push source node into OPEN
        OPEN.append(nSource)
        # process until OPEN is empty
        # Or until the route is found
        while(len(OPEN) > 0):
            curIdx = self.getMinF(OPEN)
            curNode = OPEN[curIdx]
            del OPEN[curIdx]

            if(curNode.row == trg[0] and curNode.col == trg[1]):
                return curNode
            for i in range(0, 4):
                r = curNode.row + dr[i]
                c = curNode.col + dc[i]
                if(r >= 0 and r < self.size and c >=0 and c < self.size and self.map[r][c] != -1):
                    dmi = curNode.g + 1
                    oIdx = self.findNode([r,c], OPEN)
                    if(oIdx >= 0):
                        Mi = OPEN[oIdx]
                        if(Mi.g <= dmi):
                            continue
                    cIdx = self.findNode([r, c], CLOSE)
                    if(cIdx >= 0):
                        Mi = CLOSE[cIdx]
                        if(Mi.g <= dmi):
                            continue
                        else:
                            OPEN.append(Mi)
                            del CLOSE[cIdx]
                    if(oIdx < 0 and cIdx < 0):
                        Mi = Node(r, c)
                        OPEN.append(Mi)
                    Mi.g = dmi
                    Mi.f = Mi.g + Mi.h(trg)
                    Mi.parent = curNode
            CLOSE.append(curNode)
        return -1
