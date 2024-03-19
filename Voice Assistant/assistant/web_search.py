import requests

def web_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    # Parse and extract relevant information from the response.
    # Display the information to the user.
