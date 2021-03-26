# import requests 


payload = {'secret_key': 'CHANGEME', 'pageurl': 'https://www.rackroomshoes.com/'}

# data = requests.get("http://127.0.0.1:5000", params=payload)

# print(await data.json())

import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:5000', params=payload) as response:

            html = await response.text()
            print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())