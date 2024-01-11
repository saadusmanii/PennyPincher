import requests
from bs4 import BeautifulSoup

def scrape_bestbuy(query):
    url = f"https://www.bestbuy.com/site/searchpage.jsp?st={query}&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp={query}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('div', class_='priceView-hero-price priceView-customer-price').find('span', class_='sr-only')
        return price_element.text.strip()

    return None

def scrape_newegg(query):
    url = f"https://www.newegg.com/p/pl?d={query}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('li', class_='price').find('strong')
        return price_element.text.strip()

    return None

def scrape_amazon(query):
    url = f"https://www.amazon.com/s?k={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        price_element = soup.find('span', class_='a-offscreen')
        return price_element.text.strip()

    return None

def main():
    query = input("Enter the name of the PC item: ")

    bestbuy_price = scrape_bestbuy(query)
    newegg_price = scrape_newegg(query)
    amazon_price = scrape_amazon(query)

    print("\nResults:")
    print(f"Best Buy: {bestbuy_price}")
    print(f"Newegg: {newegg_price}")
    print(f"Amazon: {amazon_price}")

if __name__ == "__main__":
    main()
