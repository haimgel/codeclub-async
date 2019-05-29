#!/usr/bin/env python3

import asyncio
import aiohttp
from urllib.parse import urljoin
from html.parser import HTMLParser

# Async/Await example:
# Fetch several web pages, verify whether all images on these pages are valid.
#

urls = ['https://www.apple.com', 'https://www.cnn.com', 'https://www.disney.com']


class MyHTMLParser(HTMLParser):
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            src = [attr[1] for attr in attrs if attr[0] == 'src']
            if len(src) > 0:
                self.images.append(urljoin(self.url, src[0]))


# aiohttp client API documentation: https://aiohttp.readthedocs.io/en/latest/client_quickstart.html
async def fetch_page(session, url):
    print('Fetching headers of', url)
    async with session.get(url, timeout=5) as response:
        print('Fetching body of', url)
        body = await response.text()
        parser = MyHTMLParser(url)
        parser.feed(body)
        for image_url in parser.images:
            print('Fetching image: ', image_url)
            async with session.get(image_url) as response:
                if response.status >= 400:
                    return False
    return True


async def fetch_pages():
    async with aiohttp.ClientSession() as session:
        futures = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*futures)
        return dict(zip(urls, results))


async def main():
    print(await fetch_pages())


asyncio.get_event_loop().run_until_complete(main())
