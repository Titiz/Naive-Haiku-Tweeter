import twython

from config import *
from constants import TWEET_LENGTH, VOWELS
import log

log.LOGGER.info("Connecting to Twitter API")
twitter = twython.Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)
log.LOGGER.info("Connected to Twitter API.")


def post_haiku(haiku: str) -> None:
    """Use the Twython API to post a haiku."""
    try:
        twitter.update_status(status=haiku)
    except twython.exceptions.TwythonAuthError as error:
        log.LOGGER.error("Posting failed with error: %s", error, exc_info=True)
