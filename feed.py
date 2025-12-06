import feedparser

class Feed():
    def __init__(self, rss_url):
        self.feed_items = []
        self.feed = feedparser.parse(rss_url)

        if self.feed.status == 200:
            for entry in self.feed.entries:
                self.feed_items.append([entry.title, entry.link])
        else:
            print("Failed to get RSS feed. Status code:", self.feed.status)