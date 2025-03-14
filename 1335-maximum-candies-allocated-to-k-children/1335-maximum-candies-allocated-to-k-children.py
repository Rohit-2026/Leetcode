class Solution(object):
    def maximumCandies(self, candies, k):
        def can_allocate(candies, k, pile_size):
            if pile_size == 0:
                return True
            total_piles = 0
            for candy in candies:
                total_piles += candy // pile_size
                if total_piles >= k:
                    return True
            return False

        if sum(candies) < k:
            return 0

        low, high = 1, max(candies)
        while low < high:
            mid = (low + high + 1) // 2
            if can_allocate(candies, k, mid):
                low = mid
            else:
                high = mid - 1

        return low