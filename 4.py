# <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
# end. 400 times is more than enough. -->

import urllib2

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

next_nothing = 12345 # If you click the photo, it gives you 12345

for i in range(400):
    response = urllib2.urlopen(url + str(next_nothing))
    the_page = response.read()
    idx = the_page.find("nothing is ")
    print the_page
    if idx == -1:

        next_nothing /= 2
    else:
        next_nothing = int(the_page[idx+len("nothing is "):])

