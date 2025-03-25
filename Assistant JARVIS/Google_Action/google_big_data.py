import requests
from bs4 import BeautifulSoup
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from Body.Advance_speak import speak

def search_and_extract(text):
    # Perform a Google search
    url = f"https://www.google.com/search?q={text}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the page.")
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first search result link
    first_result = soup.find('div', class_='g')
    if first_result:
        link = first_result.find('a')['href']
        
        # Fetch the first result page
        result_page = requests.get(link, headers=headers)
        
        if result_page.status_code != 200:
            print("Failed to retrieve the result page.")
            return ""
        
        result_soup = BeautifulSoup(result_page.text, 'html.parser')
        
        # Extract text from the webpage
        webpage_text = ' '.join([p.get_text() for p in result_soup.find_all('p')])
        
        # Extract and print the first 8-9 sentences from the webpage text
        sentences = re.split(r'(?<=[.!?])\s', webpage_text)
        result_text = '. '.join(sentences[:9])
        return result_text
    
    return "No results found."

def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

def deep_search(text):
    query = text
    extracted_text = search_and_extract(query)
    
    if extracted_text:
        speak(summarize_text(extracted_text))
        return 
    
    return "No content found."

# Example usage

