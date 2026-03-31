import petl as etl

# Load portfolio data
portfolio_data = etl.fromcsv('portfolio.csv')

# Analyze overlap between portfolios

def analyze_overlap(portfolio1, portfolio2):
    overlap = etl.intersect(portfolio1, portfolio2)
    return overlap

# Example usage of the analyze_overlap function
# Assuming portfolio1 and portfolio2 are loaded as ETL tables
# overlap_result = analyze_overlap(portfolio1, portfolio2)

# Save results to a new CSV file
# etl.tocsv(overlap_result, 'overlap_analysis.csv')

if __name__ == '__main__':
    print('Portfolio analysis module loaded.')