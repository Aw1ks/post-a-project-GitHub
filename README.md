# Counting clicks on links

## Description
This project reduces links and displays the number of clicks on them. This project uses libraries such as: [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [argparse](https://docs.python.org/3/library/argparse.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [os](https://docs.python.org/3/library/os.html) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html).

## Requests
Requests is a simple but elegant HTTP library. 
```
import requests

def shorten_link(headers, url):
    bit_url = 'https://api-ssl.bitly.com/v4/shorten'

    params = {"long_url": url}

    response = requests.post(bit_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['link']

```
