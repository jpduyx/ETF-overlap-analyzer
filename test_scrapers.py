import unittest

class TestPortfolioAnalysis(unittest.TestCase):

    def setUp(self):
        self.portfolio = {'IE0009HF1MK9': 70, 'IE0003R87OG3': 10, 'IE00BF2B0L69': 10}

    def test_portfolio_total(self):
        total = sum(self.portfolio.values())
        self.assertEqual(total, 100, "Total portfolio allocation should be 100%.")

    # Add more tests as needed for portfolio analysis

if __name__ == '__main__':
    unittest.main()  
