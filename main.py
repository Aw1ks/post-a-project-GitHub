import os
import requests
from urllib.parse import urlparse


def shorten_link(bitly_token, url):
    bit_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': bitly_token,
    }

    params = {
        "long_url" : url,
    }

    response = requests.post(bit_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitly_token, bitlink):
    bit_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    
    headers = {
        'Authorization': bitly_token,
    }

    params = {
        'unit' : 'month',
        'units' : '-1',
    }

    response = requests.get(bit_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitly_token, url):
    bit_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {
        'Authorization': bitly_token
    }
    
    response = requests.get(bit_url, headers=headers)
    return response.ok


def main():
    bitly_token = os.environ['BITLY_TOKEN']
    url = input("Введите ссылку: ")
    parsed_url = urlparse(url)
    comb_path = f'{parsed_url.netloc}{parsed_url.path}'
    try:
        if is_bitlink(bitly_token, comb_path):
            print(count_clicks(bitly_token, comb_path))
        else:
            print(shorten_link(bitly_token, url))
    except requests.HTTPError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()