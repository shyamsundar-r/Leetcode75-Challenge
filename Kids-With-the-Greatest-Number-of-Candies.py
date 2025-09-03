class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mCandies = max(candies)
        return [k+extraCandies>=mCandies for k in candies]
