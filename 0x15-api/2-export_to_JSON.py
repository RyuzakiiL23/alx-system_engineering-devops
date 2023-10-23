#!/usr/bin/python3
"""Python script that use a given REST API and create a CSV file"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = eval(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url).text
    res_list = json.loads(response)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(user_url).text
    user_dict = json.loads(user_response)
    user_name = user_dict["username"]

    new_res_list = []
    for d in res_list:
        new_elem = {'task': d['title'], 'completed': d['completed'],
                    "username": user_name}
        new_res_list.append(new_elem)
    file_path = "{}.json".format(sys.argv[1])
    data = {}
    data[sys.argv[1]] = new_res_list

    with open(file_path, "w") as file:
        json.dump(data, file)
