#!/usr/bin/env python3

import requests
import re
import urllib.parse as urlparse
from pip._vendor.distlib.compat import raw_input

url = raw_input("enter URl in proper format(like - 'https://www.google.com'): ")   # use metasploitable mutillidae for testing
target_links = []


def extract_links(urls):
    response = requests.get(urls)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))
    # () divides in subparts, ?: to non matching  ? in 2nd, make it non greedy and it will match only till first"


def crawl(urls):
    try:
        links = extract_links(urls)
        for link in links:
            link = urlparse.urljoin(urls, link)

            if "#" in link:
                link = link.split("#")[0]

            if url in link and link not in target_links:
                target_links.append(link)
                print(link)
                crawl(link)

    except KeyboardInterrupt:
        print("\n Stopping Crawler")
        exit()


crawl(url)


