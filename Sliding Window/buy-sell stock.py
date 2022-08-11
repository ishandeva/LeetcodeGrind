 
def maxProfit(prices: list[int]) -> int:
    
    MaxProfit = 0
    windowStart = 0 #Buy
    windowEnd = 1 #Sell
    
    while windowEnd < len(prices):   
        
        #Checking if it's profitable 
        if prices[windowStart] < prices[windowEnd]:
            
            #Calc the profit
            currentProfit = prices[windowEnd] - prices[windowStart]
            
            #Update the maximum profit
            if currentProfit > MaxProfit:
                MaxProfit = currentProfit
        
        #If left > right then:         
        else: 
            windowStart = windowEnd
            
        windowEnd += 1
            
    return MaxProfit

#Driver:
print(maxProfit(prices = [2,1,4]))