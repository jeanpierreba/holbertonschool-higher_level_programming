#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the value of the variable """


if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
