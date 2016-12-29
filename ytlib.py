#!/usr/bin/env python3

import urllib.request, lxml.html

YOUTUBE_BASE_URL = 'https://www.youtube.com'
YOUTUBE_SEARCH_URL = YOUTUBE_BASE_URL + '/results?search_query={0}' 
XPATH_SEARCH_RESULTS = '//a[contains(@class, "yt-uix-tile-link")]'

def html_get(url):
    obj = urllib.request.urlopen(url)
    return lxml.html.parse(obj)

def search(string):
    string = urllib.parse.quote_plus(string)        # escape the string :)
    url = YOUTUBE_SEARCH_URL.format(string)         # get search url
    obj = html_get(url)
    global results
    results = []
    for item in obj.xpath(XPATH_SEARCH_RESULTS):
        res = {}
        res['title'] = item.get('title')
        res['url'] = YOUTUBE_BASE_URL + item.get('href')
        try:
            res['id'] = _get_id(item.get('href'))
            results.append(res)
        except KeyError:pass
            #print("[WARNING] Could not parse url {0}, skipping...".format(item.get('href')))
    return results

def _get_id(url):
    query = urllib.parse.urlsplit(url).query
    return urllib.parse.parse_qs(query)['v'][0]

def search1(string):
    return search(string)[0]

def tostring(item):
    return "{0} [{1}]".format(item['title'], item['id'])
