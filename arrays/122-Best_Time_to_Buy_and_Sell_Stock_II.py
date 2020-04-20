'''


Problem solving:


'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            stockInHand, checks the current value of stock you have.
            totalProfit to store profit.
            currentProfit to calculate stockInHand profit
            
            If no stock in hand,
                if the next element is larger than current element,
                    buy currentEleemnt
            If stock in hand,
                if next element is smaller than current element
                    sell currentElement
                    increase totalProfit
            
                if next element is larger than current element
                    continue
                    
            if next element is larger than current element
                    sell current element
                    increase totalProfit
                
        '''
        stockInHand = None
        totalProfit = 0
        tempProfit = 0        
        
        for i in range(len(prices)-1):
            currentStock = prices[i]
            nextStock = prices[i+1]
            if stockInHand == None:
                if currentStock < nextStock:
                    stockInHand = currentStock
            else:
                if stockInHand < currentStock and currentStock > nextStock:
                    totalProfit += currentStock - stockInHand
                    stockInHand = None
        
        if stockInHand != None:
            if prices[-1] > stockInHand:
                totalProfit += prices[-1] - stockInHand
        return totalProfit
        
        