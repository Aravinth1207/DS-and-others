def maximumToys(prices, k):
    # Write your code here
    SUM = 0
    count = 0
    prices.sort()
    for i in prices:
        if SUM<=k:
            SUM += i 
            count+=1
            if SUM > k: 
                count-=1
                break
    
    return count


prices =[ 1 ,12, 5, 111, 200 ,1000 ,10]
k = 50
print(maximumToys(prices, k))