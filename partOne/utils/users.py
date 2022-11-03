from operator import itemgetter

users = [
    {"name": "test",
     "email": "iamtestinkr@gmail.com",
     "password": "10Namsau",
     "first_name": "long",
     "last_name": "tran"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
