import psaw
import os
import requests
import string
import random
from psaw import PushshiftAPI


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_letters+string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

api = PushshiftAPI()

sub = input("what subreddit?: ")
lim = int(input("what's the limit? (0 for none, will take a while): "))

if lim > 0:
    cool = list(api.search_submissions(
        subreddit=(str(sub)),
        filter=['url', 'title'],
        limit=(int(lim))
        ))
elif lim == 0:
    cool = list(api.search_submissions(
        subreddit=(str(sub)),
        filter=['url', 'title'],
        ))


length = len(cool)-1
curleng = length

print("all done getting data: "+str(len(cool))+" links collected")

badlinks = []

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

while curleng >= 0:
    url = cool[curleng].url
    if ((".jpg" in url) or (".png" in url)
    or (".jpeg" in url) or (".gif" in url)
    or (".mp4" in url) or (".ico" in url)
    ):
        if (".jpg" in url):
            ext="jpg"
        elif (".png" in url):
            ext="png"
        elif (".jpeg" in url):
            ext="jpeg"
        elif (".gif" in url):
            ext="gif"
        elif (".mp4" in url):
            ext="mp4"
        elif (".ico" in url):
            ext="ico"

        name = cool[curleng].title
        name = ''.join(c for c in name if c in valid_chars)

        try:
            rstring = randomString(10)
            r = requests.get(url, allow_redirects=True)
            open(name+" "+rstring+"."+ext, 'wb').write(r.content)
            print("success: "+url+' ("'+name+'", random string: '+rstring+')')
        except:
            print("error: "+url)
            badlinks.append(url)
        
        
    
    else:
        print("fail: "+url)
        badlinks.append(url)
        
    curleng=curleng-1
    
print("coool it's done")

if (len(badlinks) != 0):
    f = open("badlinks.txt", 'w+')
    f.write("")
    for link in badlinks:
        try:
            f = open("badlinks.txt", 'a')
            f.write(link+"\n")
        except:
            print("there's been an error with a link, won't add it to the list")
    print("a file containing the bad links has been created")
input("press enter to leave")
