import requests
from bs4 import BeautifulSoup

def search_brain(text):
    # Prepare the URL for Google search
    url = f"https://www.google.com/search?q={text}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send GET request
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code != 200:
        return f"Failed to retrieve results. Status code: {response.status_code}"

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first result
    first_result = soup.find('h3')  # Search for the title

    if not first_result:
        return "No results found."

    # Get the text of the first result
    print(first_result.get_text().strip())
    return None

# Example usage
