import requests
from bs4 import BeautifulSoup

def search_google(query):
    # Build the URL for the Google search
    query = query.replace(' ', '+')
    url = 'https://www.google.com/search?q=' + query

    # Send the GET request to the Google search URL
    response = requests.get(url)

    # Check the response status code
    if response.status_code != 200:
        return None

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first link in the search results
    result = soup.find('div', {'class': 'g'})
    link = result.find('a')['href']

    # Return the first result link
    return link

# Ask the user for the search query
query = input('Enter a search query: ')

# Search for the query using the search_google() function
result = search_google(query)

# Print the first result link
print('First result link:', result)
