#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:31:54 2019

@author: krishna
"""

import feedparser

url = "http://feeds.bbci.co.uk/news/rss.xml"
url = 'http://rss.cnn.com/rss/edition.rss'

def get_news(url):
    
    feed = feedparser.parse(url)
    first_article = feed['entries'][0]
    for  i in first_article:
        print(i)
    for media in first_article:
        #print(m.links)
        pass
    print(first_article.get("links"))
    print(first_article.get("link"))
    #print(first_article.media_content[0]['url'])
    #print(first_article.get("published"))
    
    
get_news(url)

