import webbrowser

def open_websites(num_sites):
    # Dictionary of websites with their URLs (without https:// and in lowercase)
    websites = {
        "dictionary.com": "www.dictionary.com",
        "merriam-webster": "www.merriam-webster.com",
        "oxford learners dictionaries": "www.oxfordlearnersdictionaries.com",
        "cambridge dictionary": "dictionary.cambridge.org",
        "collins dictionary": "www.collinsdictionary.com",
        "thesaurus.com": "www.thesaurus.com",
        "wikipedia": "en.wikipedia.org",
        "google": "www.google.com",
        "amazon": "www.amazon.com",
        "youtube": "www.youtube.com",
        "twitter": "www.twitter.com",
        "facebook": "www.facebook.com",
        "reddit": "www.reddit.com",
        "stack overflow": "stackoverflow.com",
        "github": "github.com",
        "medium": "medium.com",
        "news": "www.bbc.com/news",
        "weather": "weather.com",
        "maps": "www.google.com/maps",
        "spotify": "www.spotify.com",
        # Add more websites as needed
    }

    # Open each website num_sites times
    for site_name, site_url in websites.items():
        for _ in range(num_sites):
            full_url = f"http://{site_url}"  # Adding http:// prefix
            webbrowser.open(full_url)
            print(f"Opened {site_name}")

# Example: Open each website 400 times
num_sites_to_open = 400
open_websites(num_sites_to_open)
