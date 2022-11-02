
import requests

response = requests.get("https://api.github.com/search/issues?q=repo:SeleniumHQ/selenium/issues+type:issue+state:open")
response.json()

open_issue = response.json().get("total_count")

print(open_issue)