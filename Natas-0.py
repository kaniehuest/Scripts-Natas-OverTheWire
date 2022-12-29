import re
import requests


def main():
    URL = "http://natas0.natas.labs.overthewire.org"
    s = requests.Session()
    s.auth = ("natas0", "natas0")
    r = s.get(URL)
    natas1_password = re.findall(r"([a-zA-Z\d]{32})", r.text) 
    print(natas1_password[0])


if __name__ == '__main__':
    main()
