from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required_char_freq = defaultdict(int)
        for i in t:
            required_char_freq[i] += 1

        window = defaultdict(int)
        cnt = 0
        min_len = inf
        min_start = -1

        # Main Business Logic
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in required_char_freq and window[s[right]] <= required_char_freq[s[right]]:
                cnt += 1
            while cnt == len(t):
                current_window_size = right - left + 1
                # print(current_window_size)
                if current_window_size < min_len:
                    min_len = current_window_size
                    min_start = left
                left_char = s[left]
                if left_char in required_char_freq and window[left_char] <= required_char_freq[left_char]:
                    cnt -= 1
                window[left_char] -= 1
                left += 1

        return "" if min_start == -1 else s[min_start : min_start + min_len]
