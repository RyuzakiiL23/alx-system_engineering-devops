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

    file_path = "{}.csv".format(sys.argv[1])
    with open(file_path, "w") as file:
        for elem in res_list:
            data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                user_id, user_name, elem["completed"], elem["title"]
            )
            file.write(data)
