class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestString = ""
        local_max_string = ""
        for  i in range(len(s)):
            if s[i] in local_max_string:
                if len(longestString) < len(local_max_string):
                    longestString = local_max_string
                local_max_string = local_max_string[local_max_string.find(s[i]) + 1:] + s[i]
            else:
                local_max_string += s[i]
        print(local_max_string)
        print(longestString)
        if len(longestString) < len(local_max_string):
            longestString = local_max_string

        return len(longestString)