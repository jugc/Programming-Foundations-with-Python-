import webbrowser
import time

# Defines the URL for "Un misil en mi placard" by Soda Stereo
url = 'https://www.youtube.com/watch?v=HtcLGfKnRVw'

# Initializes the counter for the number of times to repet the sequence
number_of_breaks = 0
total_breaks = 3
work_time = 5       # in seconds
print "This program started on "+time.ctime()
while number_of_breaks < total_breaks:
    time.sleep(work_time)
    webbrowser.open(url)
    number_of_breaks = number_of_breaks + 1
