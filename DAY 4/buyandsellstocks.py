# To find the maximum profit by buying a stock at a low price and selling it on a later day at a higher price
prices = [7, 1, 5, 3, 6, 4,]
lowest = prices[0]      # Assume first price is lowest
profit = 0

for i in range(1, len(prices)):
    if prices[i] < lowest:
        lowest = prices[i]

    current_profit = prices[i] - lowest

    if current_profit > profit:
        profit = current_profit

print(profit)