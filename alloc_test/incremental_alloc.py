import time

allocs = []
while True:
    allocs.append(bytearray(8*1024*1024))
    time.sleep(1)
