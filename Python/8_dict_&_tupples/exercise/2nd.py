stock = {
    "info" : [600,630,620],
    "ril" : [1430,1490,1567],
    "mil" : [234,180,160]
}

def print_stock():
    for stock ,prices in stock.items():
        avg_price = sum(prices)/ len(prices)
        print(f"{stock} ==> {prices} ==> avg: {avg_price:.2f}")