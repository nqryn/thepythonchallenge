
# Step 1
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for m in message:
	m = (ord(m) + 2) % ord('a') + ord('a')
	print(chr(m), end='')

# Step 2
url = 'map'
for m in url:
	m = (ord(m) + 2) % ord('a') + ord('a')
	print(chr(m), end='')