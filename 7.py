from PIL import Image

im = Image.open("oxygen.png") 
pixels = list(im.getdata())
width, height = im.size

my_list = [[0, 0]]
cnt = 0
for x in range(width * (height/2), width * (height/2 + 1)):
    r, g, b, a = pixels[x]
    if r == g == b:
        if my_list[cnt][0] == r:
            my_list[cnt][1] += 1
        else:
            my_list.append([r, 1])
            cnt += 1
# Step 1
print "".join([unichr(let[0]) if let[1] == 7 else 2*unichr(let[0]) for let in my_list])

# Step 2
next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(l) for l in next_level))