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


Explanation of the Solution

This problem requires us to find the smallest substring in s that contains all characters of t, including duplicates. We solve this using the Sliding Window technique.


---

Step-by-Step Breakdown

1. Understanding the Sliding Window Approach

The Sliding Window technique works by:

1. Expanding the right pointer (r) to include more characters until the substring is valid.


2. Shrinking the left pointer (l) to minimize the window while still keeping all required characters.




---

2. Initializing Variables

countT = Counter(t)  # Stores the frequency of characters in t
window = {}          # Stores character frequencies in the current window
have, need = 0, len(countT)  # 'have' tracks matched chars, 'need' is the required unique chars
res, resLen = [-1, -1], float("inf")  # Store the best window found
l = 0  # Left pointer of the window

countT counts the frequency of characters in t.

window keeps track of the characters in our current window.

have tracks how many required characters are fully matched.

need is the total number of unique characters in t that must be present.

res stores the best window found so far.

l is the left pointer for the sliding window.



---

3. Expanding the Right Pointer (r)

for r in range(len(s)):  # Right pointer expands
    c = s[r]
    window[c] = 1 + window.get(c, 0)  # Add character to window

We iterate over s, expanding the window by adding s[r] to window.


if c in countT and window[c] == countT[c]:
    have += 1  # Only increase 'have' when a character frequency matches t

If s[r] is in t and the frequency in window matches countT, we increase have.



---

4. Shrinking the Left Pointer (l)

Once have == need, the window contains all characters in t. Now, we try to shrink it.

while have == need:
    if (r - l + 1) < resLen:  # Update result if we found a smaller valid window
        res = [l, r]
        resLen = r - l + 1

If the current window is smaller than the best found, update res and resLen.


window[s[l]] -= 1  # Remove leftmost character from window
if s[l] in countT and window[s[l]] < countT[s[l]]:
    have -= 1  # If removing this character makes window invalid, decrement 'have'
l += 1  # Move the left pointer forward

We remove s[l] from window and check if it makes the window invalid (i.e., if it drops below the required frequency).

If so, have decreases.

Move the left pointer (l) forward to try and find a smaller valid window.



---

5. Return the Smallest Window

l, r = res
return s[l:r+1] if resLen != float("inf") else ""

If we found a valid window, return it.

Otherwise, return an empty string ("").



---

Time Complexity Analysis

Why O(m + n)?

We iterate over s once with r (O(m)).

The left pointer l moves at most m times (O(m)).

We only use Counter (O(n)) to track frequencies in t.


Thus, the overall complexity is O(m + n).


---

Example Walkthrough

Example 1

Input:

s = "ADOBECODEBANC"
t = "ABC"

Execution Steps:

Output: "BANC"


---

Edge Cases Handled

1. No valid window exists → Return "" (e.g., s = "a", t = "aa").


2. Entire string is the answer → Works correctly (e.g., s = "a", t = "a").


3. Large input sizes → Efficient O(m + n) approach handles it well.




---

Key Takeaways

Sliding window expands (r moves right) and shrinks (l moves right).

Two dictionaries track character frequencies.

Only update have when a character frequency fully matches.

Once have == need, try to minimize the window.

Time complexity is O(m + n), making it optimal for large inputs.


This approach ensures the minimum substring containing all of t is found efficiently!


To solve this problem efficiently, we can use the Sliding Window technique with a two-pointer approach. Below is the Python solution that runs in  time.


---

Code Implementation

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Frequency count of characters in `t`
        t_count = Counter(t)
        required = len(t_count)
        
        # Two pointers for the sliding window
        l, r = 0, 0
        # Formed tracks how many unique characters in `t` are currently satisfied in the window
        formed = 0
        # Frequency count of characters in the current window
        window_count = {}
        
        # (window length, left pointer, right pointer)
        ans = float("inf"), None, None
        
        while r < len(s):
            # Add the character at position `r` to the window
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            
            # If the current character's frequency matches its frequency in `t`, update `formed`
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to contract the window until it ceases to be "desirable"
            while l <= r and formed == required:
                char = s[l]
                
                # Update the answer if this window is smaller than the previous best
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # Remove the character at position `l` from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                # Move the left pointer forward
                l += 1
            
            # Expand the window by moving the right pointer forward
            r += 1
        
        # Return the smallest window, or an empty string if no valid window exists
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


---

Explanation

1. Frequency Count of t:

Use a Counter to store the frequency of each character in string t.



2. Sliding Window:

Two pointers, l (left) and r (right), are used to maintain a sliding window in string s.

As the right pointer moves, characters are added to the window. If a character's frequency matches the required frequency in t, increment the formed counter.

When all required characters are satisfied (formed == required), the window is "desirable."



3. Contracting the Window:

To minimize the window size, move the left pointer (l) forward while maintaining the "desirable" property.

If removing a character from the window violates the "desirable" property, decrement formed and stop contracting.



4. Updating the Result:

Track the smallest window using a tuple (window_length, left, right). Update it whenever a smaller valid window is found.



5. Result:

Once the loop ends, if no valid window is found, return an empty string. Otherwise, return the substring corresponding to the smallest window.





---

Complexity Analysis

1. Time Complexity: 

Both pointers traverse the string s at most once, resulting in  for the sliding window.

The Counter operations for string t take .

Overall complexity is .



2. Space Complexity: 

 for the Counter to store the frequency of t.

 for the window_count dictionary, where  is the number of unique characters in s.





---

Example Walkthrough

Example 1:

Input:

s = "ADOBECODEBANC"
t = "ABC"

Steps:

1. t_count = {'A': 1, 'B': 1, 'C': 1}, required = 3


2. Expand the window with r:

Window: "ADOBEC", formed = 3 (contains "A", "B", "C").

Contract by moving l, smallest window: "BANC".



3. Result: "BANC"



Output:

"BANC"

Example 2:

Input:

s = "a"
t = "a"

Steps:

1. t_count = {'a': 1}, required = 1


2. Window: "a", formed = 1.


3. Result: "a"



Output:

"a"

Example 3:

Input:

s = "a"
t = "aa"

Steps:

1. t_count = {'a': 2}, required = 1


2. No valid window exists.



Output:

""

