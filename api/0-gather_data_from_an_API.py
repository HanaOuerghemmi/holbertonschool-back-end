#!/usr/bin/python3
""" todos from user"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(
        url + "todos", params={"userId": argv[1]}).json()
    finished = []
    for to in todos:
        if to.get("completed") is True:
            finished.append(to.get("title"))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get("name"), len(finished), len(todos)))

    for fin in finished:
        print("\t {}".format(fin))
