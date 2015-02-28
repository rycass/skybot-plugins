import random
import time
import re
from time import strptime, strftime
from urllib import quote, urlencode

from util import hook, http

import twitter
from twitter import TwitterError


@hook.api_key('vox')
@hook.command
def vox(inp, api_key=None):
    ".vox <text>/undo/rt <url> -- " \
        "Tweet <text>/Undo last tweet/Retweet <URL>"

    if not isinstance(api_key, dict) or any(key not in api_key for key in
                                            ('consumer', 'consumer_secret', 'access', 'access_secret', 'my_name')):
        return "error: api keys not set"

    rt = re.match(r'https?://(mobile.)?twitter.com/(#!/)?([_0-9a-zA-Z]+)/status/(?P<id>\d+)', inp)

    api = twitter.Api(consumer_key=api_key['consumer'], consumer_secret=api_key['consumer_secret'], access_token_key=api_key['access'], access_token_secret=api_key['access_secret'])
    
    if inp.lower() == "undo":
        try:
            twote = api.GetUserTimeline(screen_name=api_key['my_name'], count=1, include_rts=True)[0]
            if (twote.GetCreatedAtInSeconds() + 3600 >= time.time()):
                text = twote.GetText()
                api.DestroyStatus(twote.GetId())
                return 'Removed tweet: ' + text
            else:
                return 'Cannot remove tweet (too old)'
        except TwitterError as e:
            return 'Cannot remove tweet: ' + e.message
    elif rt:
        try:
            api.PostRetweet(original_id=int(rt.group('id')))
            return 'Retweeted: ' + api.GetStatus(id=int(rt.group('id'))).GetText()
        except TwitterError as e:
            return 'Cannot retweet: ' + e.message
    else:
        try:
            status = api.PostUpdate(inp)
            return 'Tweeted: ' + inp
        except TwitterError as e:
            return 'Cannot create tweet' + e.message

    return
