import base64

to_encode = raw_input("Base 64 this 20 times:")

for x in range(20):
	to_encode = base64.b64encode(to_encode)

print to_encode