def maximumToys(prices, k):
    """Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

    maximumToys has the following parameter(s):

    prices: an array of integers representing toy prices
    k: an integer, Mark's budget"""

    prices.sort()
    counter = 0
    gifts = 0
    for p in prices:
        if p + counter < k:
            counter += p
            gifts += 1 
    
    return gifts