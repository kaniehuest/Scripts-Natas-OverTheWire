import re
import requests

def get_natas1_password():
    URL = "http://natas0.natas.labs.overthewire.org"
    s = requests.Session()
    s.auth = ("natas0", "natas0")
    r = s.get(URL)
    natas1_password = re.findall(r"([a-zA-Z\d]{32})", r.text) 
    print("[!] The password for Natas 1 is: " + natas1_password[0])
    return natas1_password[0]


if __name__ == '__main__':
    get_natas1_password()
