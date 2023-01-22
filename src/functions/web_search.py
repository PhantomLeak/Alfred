import webbrowser

def search_web(search_request: str = None):
    success_message = 'Search Was Successful'

    try:
        url = create_search_url(search_request)
        webbrowser.open(url)
    except Exception as e:
        print(str(e))
        success_message = 'Search Was Unsuccessful'

    return success_message

# Take user search string and return a working URL
def create_search_url(url: str = None):
    search_site = ''

    if url.startswith('open'):
        search_site = split_string_url(url)

        # Create working url
        if '.' in search_site:
            search_site = f"https://{search_site}"
        else:
            search_site = f"https://{search_site}.com"

    return search_site

def split_string_url(url: str = None, split_itr: str = None):
    split = url.split(split_itr)

    url_string = split[1]

    formatted_url_string = "".join(url_string.split())

    return formatted_url_string