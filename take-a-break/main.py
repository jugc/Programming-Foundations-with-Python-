import webbrowser
import time

# Defines the URL for "Un misil en mi placard" by Soda Stereo
url = 'https://www.youtube.com/watch?v=HtcLGfKnRVw'

# Initializes the counter for the number of times to repet the sequence
counter = 1;
while counter < 4:
    time.sleep(10)
    webbrowser.open(url)
    
