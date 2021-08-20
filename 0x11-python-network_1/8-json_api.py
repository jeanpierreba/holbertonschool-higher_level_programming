#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    try:
        response = requests.posts("http://0.0.0.0:5000/search_user", data)
        to_json = response.json()
        if not to_json:
            print("No result")
        else:
            print("[{}] {}".format(to_json.get("id"), to_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
