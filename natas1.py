import re
import requests
from halo import Halo


def get_natas2_password(natas1_password):
    URL = "http://natas1.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 2 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    s = requests.Session()
    s.auth = ("natas1", natas1_password)
    r = s.get(URL)
    natas2_password = re.findall(r"([a-zA-Z\d]{32})", r.text)[1]

    spinner.succeed(text="The password for natas 2 is: " + natas2_password)

    return natas2_password


if __name__ == '__main__':
    natas1_password = ""  # Put here the password for natas1 here
    get_natas2_password(natas1_password)
