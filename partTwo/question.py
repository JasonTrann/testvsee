import json
import math
import requests

response = requests.get("https://api.github.com/orgs/SeleniumHQ/repos")
response.json()

repo_name = response.json()
# most_watchers = max(repo_name,key=lambda i:i['watchers_count'])
# print(most_watchers)

# Question C:
# most_watchers = max(repo_name,key=lambda i:i['watchers_count'])
# print("The repo which most open issue is: ", most_watchers.get('name'), "which have",  most_watchers.get('watchers_count'), "watcher")


# # Question A:
# for i in range(19):
#     open_issues_list = repo_name[i].get('open_issues_count')
#     # print(repo_name[i].get('open_issues_count'))
#
#     # print(type(open_issues_list))
#
#     res = [int(x) for a, x in enumerate(str(open_issues_list))]
#     # print(res)
#     b = ''.join(str(res).split(','))
#     print(b)

    # int_list = str(open_issues_list)
    #
    #
    # this_list = list(int_list)
    #
    # res = list(map(int, this_list))
    # print(res)


    # for a in range(0, len(this_list)):
    #     this_list[a] = int(this_list[a])
    #
    # print(str(this_list))

    # total = 0
    # for a in this_list:
    #     total = total + a
    #     print(total)
# # #
#
# A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
# print(A)
# # Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0
# tong = 0
# # Vòng lặp for, a là biến lặp
# for a in A:
#      tong = tong+a
# # Đầu ra: Tổng các số là 55
# print("Tổng các số là", tong)
