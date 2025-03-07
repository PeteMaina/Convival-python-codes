'''
code by Pete Maina

Get to know a work around with APIs by
- Sending the data to the API
- Parsing the data
in this example the code will just send data to an API and store it.
the data incldes title, body and userId, they are fake obviously for experimental purposes
'''
#Import neccesary libraries

#pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python API Example",
    "body": "Learning how to send API requests in Python.",
    "userId": 1
}

response = requests.post(url, json=data)  # Sending JSON data

if response.status_code == 201:  # 201 means created successfully
    print("Post created successfully!")
    print(response.json())  # Print the response
else:
    print(f"Error: {response.status_code}")
