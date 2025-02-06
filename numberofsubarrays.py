class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = 0
        even = 1  
        prefix_sum = 0
        res = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
            res %= MOD
        return res
    