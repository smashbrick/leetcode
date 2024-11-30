class Solution:
    def maxProfit(self, prices) -> int:
        maxCount = 0
        R = 1
        L = 0
        while R < len(prices):
            print(R)
            print(len(prices))
            if prices[L] < prices[R]:
                Profit = prices[R] - prices[L]
                if maxCount < Profit:
                    maxCount = Profit
            else:      
                L += 1
                print("L: ", L)
            R +=1
        return maxCount


a = Solution()

print(a.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))