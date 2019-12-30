import psaw
from psaw import PushshiftAPI
api = PushshiftAPI()

sub = input("sub?: ")
lim = int(input("limit?: "))

if lim:
	gg = list(api.search_submissions(
                            subreddit=sub,
                            filter=['url'],
                            limit=lim))
else:
	gg = list(api.search_submissions(
                            subreddit=sub,
                            filter=['url'],
                            ))
print("completed grabbing "+str(len(gg))+" links,")
print("creating file...")
f = open("links.txt", 'w+')
f.write("")
print("adding links to file...")
miss = 0
for g in gg:
	try:
		f = open("links.txt", 'a')
		f.write(g.url+"\n")
	except:
		miss=miss+1
		print("oof there's an error, hope you don't mind too much that there's "+str(miss)+" missing")
input("all done, press enter to quit")