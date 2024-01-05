import re
myString = "This is my tweet check it out http://tinyurl.com/blah"
match = re.search("(?P<url>https?://[^\s]+)", myString)
if match is not None: 
    print (match.group("url"))
    print(match)