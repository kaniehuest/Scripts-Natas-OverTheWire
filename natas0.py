import re
import requests
from halo import Halo


def get_natas1_password():
    URL = "http://natas0.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 1 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas0", "natas0")
    response = session.get(URL)
    natas1_password = re.findall(r"([a-zA-Z\d]{32})", response.text)[0]

    spinner.succeed(text="The password for natas 1 is: " + natas1_password)

    return natas1_password


if __name__ == '__main__':
    get_natas1_password()
