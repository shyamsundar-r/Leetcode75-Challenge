# Problem Name
# 1768. Merge Strings Alternately (LeetCode)

# Problem Statement
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If one string is longer, append the remaining characters of the longer string to the merged result.

# Input:
# word1 = "abc", word2 = "pqr"
# Output:
# "apbqcr"

# Approach
# Use two pointers (i for word1, j for word2).
# Append characters alternately (word1[i], then word2[j]) while both have characters left.
# If one string is longer, append the remaining characters of that string.
# Return the merged result.

#Code
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ''
        
        # Merge alternately
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        
        # Append remaining characters
        while i < len(word1):
            res += word1[i]
            i += 1
        while j < len(word2):
            res += word2[j]
            j += 1
        return res

# Example Walkthrough

# Input:
# word1 = "abc", word2 = "pqrstu"

# Step-by-step:
# Take a from word1, p from word2 → "ap"
# Take b from word1, q from word2 → "apbq"
# Take c from word1, r from word2 → "apbqcr"
# word1 is finished, append remaining "stu" from word2 → "apbqcrstu"

# Final Output:
# "apbqcrstu"

# Complexity Analysis
# Time Complexity: O(n + m)
# where n = len(word1), m = len(word2)
# We iterate through both strings once.
# Space Complexity: O(n + m)
# Result string stores all characters.
