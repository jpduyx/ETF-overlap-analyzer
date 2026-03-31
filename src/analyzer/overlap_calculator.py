class OverlapCalculator:
    def __init__(self, holdings_a, holdings_b):
        self.holdings_a = holdings_a
        self.holdings_b = holdings_b

    def calculate_overlap(self):
        overlap = {}
        total_a = sum(self.holdings_a.values())
        total_b = sum(self.holdings_b.values())
        
        for stock in self.holdings_a:
            if stock in self.holdings_b:
                overlap_percentage_a = (self.holdings_a[stock] / total_a) * 100
                overlap_percentage_b = (self.holdings_b[stock] / total_b) * 100
                overlap[stock] = {
                    'holding_a': self.holdings_a[stock],
                    'holding_b': self.holdings_b[stock],
                    'percentage_a': overlap_percentage_a,
                    'percentage_b': overlap_percentage_b
                }
                
        return overlap

# Example usage:
if __name__ == "__main__":
    holdings_a = {'AAPL': 50, 'GOOGL': 25, 'MSFT': 25}
    holdings_b = {'AAPL': 40, 'TSLA': 30, 'GOOGL': 30}
    
    calculator = OverlapCalculator(holdings_a, holdings_b)
    overlap = calculator.calculate_overlap()
    print(overlap)