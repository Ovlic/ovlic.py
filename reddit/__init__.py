import random
import asyncpraw as praw
from config import *

async def imagefetch(subreddits:list, total:int=1, nsfw:bool=False):
    print(reddit.read_only)
    thesr = random.choice(subreddits)
    loopforimg = True
    while loopforimg:
        sr = await reddit.subreddit(thesr)
        sm = await sr.random()
        if not sm.is_self and not sm.over_18:
            slink = sm.url
            if ".png" in slink or ".jpg" in slink or ".jepg" in slink or ".gif" in slink or ".gifv" in slink: loopforimg = False   
    slink = sm.url
    return sm
    
    
