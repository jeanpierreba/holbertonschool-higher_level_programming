#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the body of the response """


from urllib.request import urlopen


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
