#!/usr/bin/python3
"""Python script that use a given REST API and create a CSV file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url).text
    res_list = json.loads(response)

    user_name = []
    for i in range(1, 11):
        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(i)
        user_response = requests.get(user_url).text
        user_dict = json.loads(user_response)
        user_name.append(user_dict["username"])

    count = 0
    new_res_list = [
            [], [], [], [], [],
            [], [], [], [], []
            ]

    for elem in res_list:
        if (elem["userId"] == count + 1):
            new_elem = {"username": user_name[count], 'task': elem['title'],
                        'completed': elem['completed']}
            new_res_list[count].append(new_elem)
        else:
            if count < 11:
                count += 1
            else:
                break

    final_dict = {str(k): v for k, v in zip(range(1, 11), new_res_list)}

    with open("todo_all_employees.json", "w") as file:
        json.dump(final_dict, file)
