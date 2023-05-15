
from queue import Queue

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        qR = Queue()
        qD = Queue()

        for i in range(n):
            if senate[i] == 'R':
                qR.put(i)
            else:
                qD.put(i)

        while not qR.empty() and not qD.empty():
            indexR = qR.get()
            indexD = qD.get()
            if indexR < indexD:
                qR.put(indexR + n)
            else:
                qD.put(indexD + n)

        return "Dire" if qR.empty() else "Radiant"
