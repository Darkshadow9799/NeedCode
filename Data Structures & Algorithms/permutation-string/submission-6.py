class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for i in range(len(s1)):
            map1[s1[i]] += 1
            map2[s2[i]] += 1

        if map1 == map2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                map2.pop(s2[l])
            map2[s2[r]] += 1
            if map1 == map2:
                return True
            l += 1
        return False




        # window_size = len(s1)
        # sortedS1 = "".join(sorted(s1))
        # for i in range(len(s2) - window_size + 1):
        #     # print(s2[i:i+window_size])
        #     if (sortedS1 == "".join(sorted(s2[i:i+window_size]))):
        #         return True
        
        # return False


