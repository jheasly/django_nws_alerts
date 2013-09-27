import feedparser

loc = 'ORC039'

def main():
    feed_url = 'http://alerts.weather.gov/cap/wwaatmget.php?x=%s' % (loc)
    print feed_url
#     feed = feedparser.parse(feed_url)
#     for entry in feed.entries:
#         print entry

if __name__ == "__main__" : main()
