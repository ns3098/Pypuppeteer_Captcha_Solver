#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Utility functions. """
import asyncio
import aiofiles
import requests
from pyppeteer.chromium_downloader import *
from requests.auth import HTTPProxyAuth


__all__ = [
    'get_event_loop',
    "save_file",
    "load_file",
    "get_page",
]

NO_PROGRESS_BAR = os.environ.get('PYPPETEER_NO_PROGRESS_BAR', '')
if NO_PROGRESS_BAR.lower() in ('1', 'true'):
    NO_PROGRESS_BAR = True  # type: ignore

win_postf = "win" if int(REVISION) > 591479 else "win32"
downloadURLs.update({
    'win32': f'{BASE_URL}/Win/{REVISION}/chrome-{win_postf}.zip',
    'win64': f'{BASE_URL}/Win_x64/{REVISION}/chrome-{win_postf}.zip',
})
chromiumExecutable.update({
    'win32': DOWNLOADS_FOLDER / REVISION / f'chrome-{win_postf}' / 'chrome.exe',
    'win64': DOWNLOADS_FOLDER / REVISION / f'chrome-{win_postf}' / 'chrome.exe',
})


def get_event_loop():
    """Get loop of asyncio"""
    if sys.platform == "win32":
        return asyncio.ProactorEventLoop()
    return asyncio.new_event_loop()


async def save_file(file, data, binary=False):
    """Save data on file"""
    mode = "w" if not binary else "wb"
    async with aiofiles.open(file, mode=mode) as f:
        await f.write(data)


async def load_file(file, binary=False):
    """Load data on file"""
    mode = "r" if not binary else "rb"
    async with aiofiles.open(file, mode=mode) as f:
        return await f.read()


async def get_page(url, proxy=None, proxy_auth=None, binary=False, verify=False, timeout=300):
    """Get data of the page (File binary of Response text)"""
    urllib3.disable_warnings()
    proxies = None
    auth = None
    if proxy and proxy_auth:
        proxies = {"http": proxy, "https": proxy}
        auth = HTTPProxyAuth(proxy_auth['username'], proxy_auth['password'])
    retry = 3  # Retry 3 times
    while retry > 0:
        try:
            with requests.Session() as session:
                session.proxy = proxies
                session.auth = auth
                response = session.get(url, verify=verify, timeout=timeout)
                if binary:
                    return response.content
                return response.text
        except requests.exceptions.ConnectionError:
            retry -= 1