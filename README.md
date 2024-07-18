# Shortening links using Bitly
## Description
This project reduces links and displays the number of clicks on them. This project uses libraries such as: [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [argparse](https://docs.python.org/3/library/argparse.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [os](https://docs.python.org/3/library/os.html) and [urllib.parse](https://docs.python.org/3/library/urllib.parse.html).
## How to install
Python3 should already be installed. Use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
It is recommended to use [virtual/venv](https://docs.python.org/3/library/venv.html)

In the folder with the project, create .the env file where you mark your [Bitly token](https://medium.com/loopring-russian/%D1%85%D0%BE%D1%82%D0%B8%D1%82%D0%B5-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D0%B2%D0%BE%D0%B9-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%82%D0%BE%D0%BA%D0%B5%D0%BD-%D0%B2%D0%BE%D1%82-%D0%BA%D0%B0%D0%BA-%D1%8D%D1%82%D0%BE-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D0%B7%D0%B0-1-%D0%BC%D0%B8%D0%BD%D1%83%D1%82%D1%83-1e4eb1afb25b)

`
apikey_bitly = here is your Bitly token
`

## How to run the file

In order to shorten the link, you need to run the file where your link will be used as an argument:

```
python main.py https://dvmn.org/modules/
```

To count clicks on a link, you need to run a file where your Bitly will be used as an argument:

```
python main.py https://bit.ly/3N9ThBf
```
