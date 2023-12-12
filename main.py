import requests
from bs4 import BeautifulSoup

def get_news_titles(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check the success of the request
    if response.status_code == 200:
        # Use BeautifulSoup for HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all article titles
        titles = soup.find_all('h2', class_='article-title')
        
        # Print the titles
        for title in titles:
            print(title.text.strip())
    else:
        print(f"Error in request: {response.status_code}")

# Example of using the web scraper
url_to_parse = 'https://example.com/news'
get_news_titles(url_to_parse)
