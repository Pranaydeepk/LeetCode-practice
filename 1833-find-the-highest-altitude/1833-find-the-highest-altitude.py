class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # altitudes,n = [0], len(gain)
        # for i in range(n):
        #     altitude = altitudes[i]+gain[i]
        #     altitudes.append(altitude)
        # return max(altitudes)        
        curr, high = 0,0
        for i in gain:
            curr += i
            high = max(high,curr)
        return high