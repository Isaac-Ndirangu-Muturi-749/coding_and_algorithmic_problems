from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = Counter(t)  # Count occurrences of characters in t
        window = {}  # Dictionary to store the window's character count
        
        have, need = 0, len(countT)  # 'have' tracks how many characters match, 'need' is the total unique characters in t
        res, resLen = [-1, -1], float("inf")  # Stores the best window indices and its length
        l = 0  # Left pointer for the sliding window

        for r in range(len(s)):  
            c = s[r]
            window[c] = 1 + window.get(c, 0)  # Add character to the window

            if c in countT and window[c] == countT[c]:  
                have += 1  # Increase 'have' when a character matches the required frequency

            while have == need:  # When all characters from t are present in the current window
                if (r - l + 1) < resLen:  # Update the result if the current window is smaller
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1  # Remove the leftmost character from the window
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1  # If removing a character causes a mismatch, decrease 'have'
                l += 1  # Move the left pointer to shrink the window

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""  # Return the minimum window substring
