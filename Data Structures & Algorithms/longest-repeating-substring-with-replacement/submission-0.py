class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        max_frequency = 0
        l = 0
        for i in range(len(s)):
            if s[i] in char_count.keys(): 
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 0
            max_frequency = max(max_frequency, char_count[s[i]])
            if  i-l - max_frequency > k:
                char_count[s[l]] -= 1
                l += 1
        
        return len(s) - l