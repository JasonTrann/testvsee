import json
import math
import requests

response = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
response.json()

repo_name = response.json()
# most_watchers = max(repo_name,key=lambda i:i['watchers_count'])


# # Question C:
# most_watchers = max(repo_name,key=lambda i:i['watchers_count'])
# print("The repo which most open issue is: ", most_watchers.get('name'), "which have",  most_watchers.get('watchers_count'), "watcher")


# Question A:
for i in range(19):
    open_issues_list = repo_name[i].get('open_issues_count')
    # print(repo_name[i].get('open_issues_count'))
    int_list = int(open_issues_list)

    suma = 0
    for suma in range(int_list):
        suma += int(int_list)
        print(int(suma))
