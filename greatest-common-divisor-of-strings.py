# Problem Name
# 1071. Greatest Common Divisor of Strings (LeetCode)

# Problem Statement
# For two strings str1 and str2, we say str1 divides str2 if and only if str2 = str1 + str1 + ... + str1 (i.e., str1 is concatenated one or more times).
# Given two strings str1 and str2, return the largest string x that divides both str1 and str2.

# Input:
# str1 = "ABCABC", str2 = "ABC"
# Output:
# "ABC"

# Approach
# The potential gcd string must be a prefix of both str1 and str2.
# Start with the shorter string as the initial candidate.
# Check if the candidate divides both strings using a helper function:
# Ensure length divisibility (len(word) % len(div) == 0).
# Verify by repeating or cycling through characters.
# If it doesn’t divide, shorten the candidate by removing the last character and check again.
# Continue until a valid divisor is found, or return "" if none exists.

# Python Code
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = str1 if len(str1) < len(str2) else str2
        def isDivisible(word, div):
            l, L = len(div), len(word)
            if L % l != 0:
                return False
            j = 0
            for i in range(L):
                if word[i] != div[j]:
                    return False
                j = (j + 1) % l
            return True
        while len(gcd) > 0:
            if isDivisible(str1, gcd) and isDivisible(str2, gcd):
                return gcd
            gcd = gcd[:-1]
        return ''
        
# Example Walkthrough

# Input:
# str1 = "ABABAB", str2 = "ABAB"

# Step-by-step:
# Start with gcd = "ABAB" (shorter string).
# Check if "ABABAB" can be formed by repeating "ABAB" → ❌ (fails).
# Reduce gcd = "ABA". Check divisibility → ❌ (fails).
# Reduce gcd = "AB". Check divisibility:
# "ABABAB" = "AB" + "AB" + "AB" ✅
# "ABAB" = "AB" + "AB" ✅
# Both divisible → return "AB"

# Output:
# "AB"

# Complexity Analysis
# Time Complexity:
# Worst case, we shrink the candidate from min(len(str1), len(str2)) down to 1.
# Each check runs in O(n + m), so worst case: O((n + m) * min(n, m)).
# Space Complexity: O(1) (just variables, no extra data structures).

# Alternative shorter approach:
# Use math.gcd and string concatenation:
# from math import gcd
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 + str1:
#             return ""
#         return str1[:gcd(len(str1), len(str2))]

