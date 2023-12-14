# Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                max_profit+=prices[i]-prices[i-1]
        return max_profit

'''
The Problem states us to find the maximum profit, we can do both buy and sell on the same day.
Our main goal here is to maximise the profit. so in that case we want to make max. profit by doing max. 
transactions,(i.e. we would want to buy and sell as quick as possible).try to make consecutive profitable transactions.
we will try to treat every point as a selling point, and a particular day could be used as a selling point
only if there is a point before that day where cost of stock is less than what it is today.
So, the problem boils down finding the max. profit if we are selling today.
let's say prices = [7,1,5,3,6,4]
Day 0 - We can't sell because there is no previous buying point.
Day 1 - We can't sell because previous day price is greater than 1. (i.e. 7 > 1) which will result in loss.
Day 2 - We can sell max profit would be (5-1) = 4
Day 3 - We can't sell because 3 < 5, also we have already made a transaction on Day 0 i.e.(1)
Day 4 - We can sell, if we buy at day 3 (5-1)+(6-3)=7
Day 5 - We can't sell because there no lower buying point before it, and also there has been already transaction
        carried out on Day 1, Day 3.
'''