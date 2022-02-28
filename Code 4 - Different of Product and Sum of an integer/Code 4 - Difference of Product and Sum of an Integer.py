class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 1
        while n != 0:
            r = n % 10
            sum = sum + r
            product = product * r
            n = n // 10
        return(product - (sum - 1))