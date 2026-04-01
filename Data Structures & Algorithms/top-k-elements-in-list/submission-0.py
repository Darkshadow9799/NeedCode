class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for num in nums:
            if num in mapp:
                mapp[num] += 1
            else:
                mapp[num] = 0
        sortedMap = sorted(mapp.items(), key = lambda items:items[1], reverse=True)
        return [x[0] for x in sortedMap][:k]

        
        