costs = []
n = int(input())

expenses = [float(input()) for i in range(n)]

total_cost = sum(costs)  
avg_costs = total_cost / n  

for i in costs:
    costs[costs.index(i)] = abs(i - avg_costs)
    
print('${:.2f}'.format(sum(costs) / 2))