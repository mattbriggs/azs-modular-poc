''' This is the example of the RSS library.'''

import datetime 
import rfeed as rss

item1 = rss.Item(
    title = "First article",
    link = "http://www.example.com/articles/1", 
    description = "This is the description of the first article",
    author = "Santiago L. Valdarrama",
    guid = rss.Guid("http://www.example.com/articles/1"),
    pubDate = datetime.datetime(2014, 12, 29, 10, 00))

item2 = rss.Item(
    title = "Second article",
    link = "http://www.example.com/articles/2", 
    description = "This is the description of the second article",
    author = "Santiago L. Valdarrama",
    guid = rss.Guid("http://www.example.com/articles/2"),
    pubDate = datetime.datetime(2014, 12, 30, 14, 15))

items = [item1, item2]

feed = rss.Feed(
    title = "Sample RSS Feed",
    link = "http://www.example.com/rss",
    description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
    language = "en-US",
    lastBuildDate = datetime.datetime.now(),
    items = items)

print(feed.rss())