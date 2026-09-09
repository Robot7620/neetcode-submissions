class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        for i in range(len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            if i>= len(s1):
                window[ord(s2[i-m]) - ord('a')] -= 1
            if window == need:
                return True
        return False
