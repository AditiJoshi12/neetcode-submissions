class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return "" 

        freq_map = {}
        for c in t:
            freq_map[c] = freq_map.get(c, 0) + 1

        freqS = {}
        left = 0

        have, need = 0, len(freq_map)

        best_window = [-1, -1]
        min_len = float("infinity")

        for right in range(len(s)):
            char = s[right]
            freqS[char] = freqS.get(char, 0) + 1

            if char in freq_map and freq_map[char] == freqS[char]:
                have += 1

            while have == need: 
                window_size = right - left + 1
                if window_size < min_len:
                    best_window = [left, right]
                    min_len = window_size

                left_char = s[left]
                freqS[left_char] -= 1 

                if left_char in freq_map and freqS[left_char] < freq_map[left_char]:
                    have -= 1
                
                left += 1

        l, r = best_window

        return s[l:r+1] if min_len != float("infinity") else ""

            
            



        