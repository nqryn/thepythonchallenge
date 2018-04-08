# <!-- zip -->
import zipfile


my_zip = zipfile.ZipFile("channel.zip")
next_nothing = 90052
comments = []

fl = {f.filename: f for f in my_zip.filelist}

while True:
    filename = str(next_nothing) + ".txt"
    fd = my_zip.open(filename)
    the_page = fd.read()
    idx = the_page.find("nothing is ")
    if idx == -1:
        print the_page
        break
    else:
        next_nothing = int(the_page[idx+len("nothing is "):])
        comments.append((next_nothing, fl[filename].comment))

print "".join([x[1] for x in comments])