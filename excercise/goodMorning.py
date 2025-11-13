import time
timestamp = time.strftime('%H:%M:%S')
timestamph = int(time.strftime('%H'))
timestampm = int(time.strftime('%M'))
timestamps = int(time.strftime('%S'))

if (timestamph >= 5 and timestamph <= 10):
    print("Good morning")
