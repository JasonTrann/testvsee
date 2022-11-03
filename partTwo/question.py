
import requests

response = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
response.json()

repo_name = response.json()

# Question C:
most_watchers = max(repo_name, key=lambda i: i['watchers_count'])
print("The repo which most open issue is: ", most_watchers.get('name'), "which have",
      most_watchers.get('watchers_count'), "watcher")

# Question A:
sum_open: int = 0
for i in range(19):
    open_issues_list = repo_name[i].get('open_issues_count')
    sum_open += open_issues_list

print("Total opne Issues is: ", sum_open)
