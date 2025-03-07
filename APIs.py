'''
code by Pete Maina

Get to know a work around with APIs by
- Getting the data from the API
- Parsing the data
in this example the code will just fetch the data from the API and print it.
the data incldes name, email and country, they are fake obviously for experimental purposes
'''
#Import neccesary libraries
import requests

url = "https://randomuser.me/api/"
response = requests.get(url)  # Sending a GET request

if response.status_code == 200:  # 200 means success
    data = response.json()  # Convert response to JSON
    user = data["results"][0]  # Extract first user
    print(f"Name: {user['name']['first']} {user['name']['last']}")
    print(f"Email: {user['email']}")
    print(f"Country: {user['location']['country']}")
else:
    print(f"Error: {response.status_code}")
