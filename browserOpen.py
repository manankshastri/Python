import time
import webbrowser

#the time when the program starts
print("The program started on "+ time.ctime())
for i in range(3):
    #time delay
    time.sleep(5)
    # after the time, this website will open
    # the website will open after every 5 seconds, 3 times
    webbrowser.open("https://www.youtube.com/watch?v=8f7wj_RcqYk")