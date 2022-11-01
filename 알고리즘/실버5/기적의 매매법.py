import sys
input = sys.stdin.readline
money = int(input())
stocks = list(map(int, input().split()))

jun_asset, sung_asset = money, money
jun_cnt, sung_cnt = 0, 0

for stock in stocks:
    if jun_asset >= stock:
        jun_cnt += (jun_asset // stock)
        jun_asset %= stock
        
for i in range(3, len(stocks)):
    if stocks[i - 3] < stocks[i - 2] < stocks[i - 1] < stocks[i]:
        sung_asset += (sung_cnt * stocks[i])
        sung_cnt = 0
    
    elif stocks[i - 3] > stocks[i - 2] > stocks[i - 1] > stocks[i]:
        sung_cnt += sung_asset // stocks[i]
        sung_asset %= stocks[i]
    
        
jun_tot = jun_asset + (jun_cnt * stocks[-1])
sung_tot = sung_asset + (sung_cnt * stocks[-1])

if jun_tot > sung_tot:
    print('BNP')
elif jun_tot < sung_tot:
    print('TIMING')
else:
    print('SAMESAME')