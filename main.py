from mail import Mail
from feed import Feed

if __name__ == "__main__":
    world_feed = Feed("https://www.econlib.org/feed/main")
    test_mail = Mail("test@test.co")
    test_mail.send(world_feed.feed_items[0])