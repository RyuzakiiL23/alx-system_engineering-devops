#!/usr/bin/python3
"""Python script that uses a given REST API and creates a JSON"""
import json
import requests
import sys


def to_json():
    all_user_data = {}

    for user_id in range(1, 11):
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response = requests.get(url)

        res_list = response.json()
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_response = requests.get(user_url)

        user_dict = user_response.json()
        user_name = user_dict["username"]

        new_res_list = []
        for elem in res_list:
            new_elem = {"username": user_name, 'task': elem['title'],
                        'completed': elem['completed']}
            new_res_list.append(new_elem)

        all_user_data[user_id] = new_res_list

    file_path = "todo_all_users.json"

    with open(file_path, "w") as file:
        json.dump(all_user_data, file)


if __name__ == "__main__":
    to_json()
