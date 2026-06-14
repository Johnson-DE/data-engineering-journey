"""import requests

response = requests.get(
    "https://api.github.com/users/octocat"
    )

print(response.text)"""

# Practice 1

"""import requests

response = requests.get(
    "https://api.github.com/users/octocat"
)

print(response.status_code)"""

# Practice 2

"""import requests

response = requests.get(
    "https://api.github.com/users/octocat"
)

print(response.text)"""

# Practice 3

"""import requests

response = requests.get(
    "https://api.github.com/users/octocat"
)

data =  response.json() 

print(data)
"""

"""Practice 4

Print:

login
id
followers
public_repos"""


"""import requests

response = requests.get(
    "https://api.github.com/users/octocat"
)

data =  response.json() 

print(data["login"])"""


#GitHub User Fetcher

"""import requests
try:
    username = (input("Enter GitHub Username: "))

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/1")

    data = response.json()

    print("UserName: ",data["name"])
    print("ID: ",data["id"])
    print("Email: ",data["email"])
except Exception as e:
    print("Error: ", e)"""
