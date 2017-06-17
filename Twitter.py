import twython

from config import *
from constants import TWEET_LENGTH, VOWELS


twitter = twython.Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)


def post_haiku(haiku: str) -> None:
    """Use the Twython API to post a haiku."""
    try:
        twitter.update_status(status=haiku)
    except twython.exceptions.TwythonAuthError as error:
        pass  # Use logging here
