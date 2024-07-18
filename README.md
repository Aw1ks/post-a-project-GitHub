# Counting clicks on links

## Description
This project reduces links and displays the number of clicks on them. This project uses libraries such as: [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [argparse](https://docs.python.org/3/library/argparse.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [os](https://docs.python.org/3/library/os.html) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html).

## Requests
```
>>> import requests
>>> r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```
