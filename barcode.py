
f = open('/dev/hidraw0')

while 1:
    c = f.read(1)
    if ord(c):
        print(ord(c))

