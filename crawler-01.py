#!/usr/bin/env python3

import asyncio
import aiohttp

# Async/Await example:
# Fetch several web pages, get their sizes.
#
# Exercise: instead of returning the size of each page, validate whether each image on the page is valid.
# See `crawler-02.py` for an example implementation.
#

urls = ['https://www.apple.com', 'https://www.cnn.com', 'https://www.disney.com']


# aiohttp client API documentation: https://aiohttp.readthedocs.io/en/latest/client_quickstart.html
async def fetch_page(session, url):
    print('Fetching headers of', url)
    async with session.get(url, timeout=5) as response:
        print('Fetching body of', url)
        return len(await response.text())


async def fetch_pages():
    async with aiohttp.ClientSession() as session:
        futures = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*futures)
        return dict(zip(urls, results))


async def main():
    print(await fetch_pages())


asyncio.get_event_loop().run_until_complete(main())
