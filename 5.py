# <!-- peak hell sounds familiar ? -->

import pickle
import urllib2

url = "http://www.pythonchallenge.com/pc/def/banner.p"
response = urllib2.urlopen(url)
the_page = response.read()
obj = pickle.loads(the_page)
for ll in obj:
    s = 0
    to_print = ""
    for t in ll:
        to_print += t[0] * t[1]
    print to_print