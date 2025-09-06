# Problem Name
# 1431. Kids With the Greatest Number of Candies (LeetCode)

# Problem Statement
# You are given an integer array candies, where each candies[i] represents the number of candies the i-th kid has.
# You are also given an integer extraCandies, denoting the number of extra candies that you can give to any kid.
# Return a boolean list of length n where result[i] is True if, after giving the i-th kid all the extra candies, they will have the greatest number of candies among all kids; otherwise False.

# Approach
# Find the maximum candies any kid currently has (mCandies = max(candies)).
# For each kid, check if their candies + extraCandies is greater than or equal to mCandies.
# If yes → that kid can reach the maximum → append True. Otherwise, append False.
# Return the result list.

# Python Code
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mCandies = max(candies)
        return [k + extraCandies >= mCandies for k in candies]

# Example Walkthrough

# Input:
# candies = [2, 3, 5, 1, 3], extraCandies = 3

# Step-by-step:
# Maximum candies = 5
# Kid 1: 2 + 3 = 5 → ✅ True
# Kid 2: 3 + 3 = 6 → ✅ True
# Kid 3: 5 + 3 = 8 → ✅ True
# Kid 4: 1 + 3 = 4 → ❌ False
# Kid 5: 3 + 3 = 6 → ✅ True

# Output:
# [True, True, True, False, True]

# Complexity Analysis
# Time Complexity: O(n)
# Finding max takes O(n).
# Iterating through kids also takes O(n).
# Space Complexity: O(n)
# We store a result list of length n.
