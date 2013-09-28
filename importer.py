#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import datetime
import dateutil.parser import parse as dateParser
from lxml import objectify, etree

loc = 'ORC039'

def main():
    feed_url = 'http://alerts.weather.gov/cap/wwaatmget.php?x=%s' % (loc)
    
    doc = objectify.parse(feed_url)
    tree = doc.getroot()
    
#     print(objectify.dump(tree))
    
    for e in tree.entry:
#         print e.title
#         print e.summary
        print 'What: %s' % e['{urn:oasis:names:tc:emergency:cap:1.1}event']
        expires = dateParser(e['{urn:oasis:names:tc:emergency:cap:1.1}expires'].text)
        print expires.strftime('%M %Y')
#         print 'Expires: %s' % datetime.datetime.strptime(e['{urn:oasis:names:tc:emergency:cap:1.1}expires'].text, '%Y-%m-%dT%H:%M:%S%z')

if __name__ == "__main__" : main()
