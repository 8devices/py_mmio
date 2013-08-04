import gpio

register = gpio.read(18)
print "Read: 0x%08X" % register

gpio.write(18, 0)
