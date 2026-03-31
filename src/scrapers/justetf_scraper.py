import requests
from bs4 import BeautifulSoup

def fetch_etf_holdings(etf_url):
    """
    Fetches the holdings data of the specified ETF from JustETF.

    Parameters:
    etf_url (str): The URL of the ETF on JustETF.

    Returns:
    dict: A dictionary containing the holdings data.
    """
    response = requests.get(etf_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    holdings = {}
    # Modify the following selectors based on the actual structure of the JustETF page
    for holding in soup.select('table tbody tr'):
        name = holding.select_one('td.name').get_text(strip=True)
        weight = holding.select_one('td.weight').get_text(strip=True)
        holdings[name] = weight
    
    return holdings

# Example usage:
if __name__ == "__main__":
    example_url = 'https://www.justetf.com/en/etf-holdings.html'  # Replace this with the actual ETF URL
    holdings_data = fetch_etf_holdings(example_url)
    print(holdings_data)