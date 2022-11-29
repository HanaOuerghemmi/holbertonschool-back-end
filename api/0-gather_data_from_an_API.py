#!/usr/bin/python3
""" todos from user"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "users/{}".format(argv[1])).json()

    finished = []
    for fin in todos:
        if fin.get("completed") is True:
            finished.append(fin)
    print("Employee {} is done with tasks ({}/{}):".format(user.get("name"),
                                                           len(finished), len(todos)))

    for fin in finished:
        print("\t {}".format(fin.get("title")))
