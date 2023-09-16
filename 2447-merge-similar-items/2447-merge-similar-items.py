class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = {}
        for x in items1:
            if x[0] not in ret:
                ret[x[0]] = x[1]
        for x in items2:
            if x[0] not in ret:
                ret[x[0]] = x[1]
            else:
                ret[x[0]] += x[1]
        result = []
        for x,y in ret.items():
            result.append([x,y])
        result.sort()
        return result