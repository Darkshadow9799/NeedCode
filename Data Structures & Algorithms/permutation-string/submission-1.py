class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        sortedS1 = "".join(sorted(s1))
        for i in range(len(s2) - window_size + 1):
            # print(s2[i:i+window_size])
            if (sortedS1 == "".join(sorted(s2[i:i+window_size]))):
                return True
        
        return False