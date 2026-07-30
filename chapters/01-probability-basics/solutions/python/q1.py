def count_ways(companies, remaining_money, idx):
    if remaining_money == 0:
        return 1
    if remaining_money < 0 or idx == len(companies):
        return 0
    
    price = companies[idx]
    return count_ways(companies, remaining_money, idx + 1) + \
           count_ways(companies, remaining_money - price, idx)

prices = [2, 3, 5, 7]
print(count_ways(prices, 10, 0))
