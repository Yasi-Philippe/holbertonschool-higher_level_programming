#!/usr/bin/python3
"""Script that consumes and processes data from an API"""


import requests
import csv


def fetch_and_print_posts():
    """Function that fetches posts from JSONPlaceholder"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(r.status_code)
    if r.status_code == 200:
        my_json_object = r.json()
        for i in my_json_object:
            print(i.get("title"))


def fetch_and_save_posts():
    """Function that fetches posts and saves them"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        my_json_object = r.json()
        my_dict = {"id" : None, "title" : None, "body" : None}
        for i in my_json_object:
            for key, value in i.items():
                if key in my_dict:
                    my_dict[key] = value
        with open("posts.csv", "w", encoding="UTF-8") as my_file:
            csv.DictWriter(my_file, my_dict.keys())

fetch_and_save_posts()
