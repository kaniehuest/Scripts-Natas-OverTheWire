import re
import requests
import base64
from halo import Halo


def get_secret(session):
    URL_SECRET = "http://natas8.natas.labs.overthewire.org/index-source.html"

    # Get the secret
    request = session.get(URL_SECRET)
    secret = re.findall(r'([a-zA-Z\d]{32})', request.text)[0]

    # Decode the secret
    secret = bytes.fromhex(secret).decode("utf-8")  # Decode the hex value
    secret = secret[::-1]  # Reverse the value
    secret = base64.b64decode(secret).decode()  # Base64 decode the value

    return secret


def get_natas9_password(natas8_password):
    URL = "http://natas8.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 9 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas8", natas8_password)

    secret = get_secret(session)

    # Get password for natas9
    data = {"secret": secret, "submit": "true"}
    request = session.post(URL, data=data)
    natas9_password = re.findall(r'([a-zA-Z\d]{32})', request.text)[1]

    spinner.succeed(text="The password for natas 9 is: " + natas9_password)

    return natas9_password


if __name__ == '__main__':
    natas8_password = ""  # Put here the password for natas8 here
    get_natas9_password(natas8_password)
