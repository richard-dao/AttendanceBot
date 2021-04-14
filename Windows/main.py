import subprocess
import schedule
from datetime import datetime, timedelta, date
from threading import Timer
# --------------------------------------------------------------------------------------------------------------- #
period1Link = "https://auhsdschools.zoom.us/j/81570374074"
period2Link = "https://auhsdschools.zoom.us/j/83717749766?pwd=cm8wNUdocU9neFpXM28rakxxY0R4QT09"
period3Link = "https://auhsdschools.zoom.us/j/85367548947"
period4Link = "https://auhsdschools.zoom.us/j/83100141993"
period5Link = "https://auhsdschools.zoom.us/j/87122384475"
period6Link = "https://auhsdschools.zoom.us/j/81886568339?pwd=UCtWL0NsVE9BOWhzSGVqMndhanBpdz09"
period7Link = "https://auhsdschools.zoom.us/j/84243151244?pwd=UG9CcWU5QTZmcm9TR2ZRWElhK0NXQT09"
cohortLink = "https://auhsdschools.zoom.us/j/87594112356?pwd=UUE3REtuRG0xdVFodUN1UGZNQmpBZz09"
pathToZoom = 'C:\\Users\\rdao2\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe' # If Mac OSX, configure 
# --------------------------------------------------------------------------------------------------------------- #

# First Calls
t_x = datetime.today()
t_0 = t_x.replace(day=t_x.day, hour=8, minute=30, second=0, microsecond=0) + timedelta(days=0) # School Start Time
deltaT = t_0 - t_x
seconds = deltaT.total_seconds()

print("Starting Day")

def cohort():
    print("Cohort")
    t_x = datetime.today()
    print(t_x)
    subprocess.Popen(pathToZoom)
    endDaySeconds = t_0.replace(day=t_0.day, hour=9, minute=45, second=0, microsecond=0)
    endDaySeconds = endDaySeconds - t_x
    endDaySeconds = endDaySeconds.total_seconds()
    subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", cohortLink]))
    y = Timer(endDaySeconds, endDay)
    y.start()  

def period1():
    subprocess.Popen(pathToZoom)
    t_x = datetime.today()
    print(date.today())
    if (date.today().weekday() == 0): # If Monday
        print("Monday")
        seconds1 = t_0.replace(day=t_0.day, hour=9, minute=0, second=0, microsecond=0) # Cohort Starts
        seconds1 = seconds1 - t_x
        seconds1 = seconds1.total_seconds()
        if (seconds1 < 0):
            x = Timer(seconds1, endDay)
            x.start()
        else:
            x = Timer(seconds1, cohort)
            x.start()
    elif (date.today().weekday() == 1 or date.today().weekday() == 2): # If Tuesday or Wednesday do 1-2-3-7, # Else do 4-5-6
        print("Tuesday/Wednesday")
        seconds1 = t_0.replace(day=t_0.day, hour=9, minute=45, second=0, microsecond=0) # Period 1 Ends
        seconds1 = seconds1 - t_x
        seconds1 = seconds1.total_seconds()
        if (seconds1 < 0):
            print("Period 1 Already Over!")
        else:
            print("Period 1")
            subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period1Link])) # Period 1 Zoom Link
        x = Timer(seconds1, pass1)
        x.start()
    else:
        print("Thursday/Friday")
        period4()

def pass1():
    print("Brunch")
    t_x = datetime.today()
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    subprocess.Popen(pathToZoom)
    pass1Seconds = t_0.replace(day=t_0.day, hour=10, minute=5, second=0, microsecond=0) # Period 2 Starts
    pass1Seconds = pass1Seconds - t_x
    pass1Seconds = pass1Seconds.total_seconds()
    y = Timer(pass1Seconds, period2)
    y.start()

def period2():
    t_x = datetime.today()
    seconds2 = t_0.replace(day=t_0.day, hour=11, minute=20, second=0, microsecond=0) # Period 2 Ends
    seconds2 = seconds2 - t_x
    seconds2 = seconds2.total_seconds()
    print(seconds2)
    if (seconds2 < 0):
        print("Period 2 Already Over!")
    else:
        print("Period 2")
        subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period2Link]))
    x = Timer(seconds2, pass2)
    x.start()

def pass2():
    print("Lunch")
    t_x = datetime.today()
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    subprocess.Popen(pathToZoom)
    pass2Seconds = t_0.replace(day=t_0.day, hour=12, minute=40, second=0, microsecond=0) # Period 3 Starts
    pass2Seconds = pass2Seconds - t_x
    pass2Seconds = pass2Seconds.total_seconds()
    print(pass2Seconds)
    y = Timer(pass2Seconds, period3)
    y.start()

def period3():
    t_x = datetime.today()
    seconds3 = t_0.replace(day=t_0.day, hour=13, minute=55, second=0, microsecond=0) # Period 3 Ends
    seconds3 = seconds3 - t_x
    seconds3 = seconds3.total_seconds()
    if (seconds3 < 0):
        print("Period 3 Already Over!")
    else:
        print("Period 3")
        subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period3Link]))
    x = Timer(seconds3, pass3)
    x.start()

def pass3():
    print("Passing Period Between Periods 3 and 7")
    t_x = datetime.today()
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    subprocess.Popen(pathToZoom)
    pass3Seconds = t_0.replace(day=t_0.day, hour=14, minute=5, second=0, microsecond=0) # Period 7 Starts
    pass3Seconds = pass3Seconds - t_x
    pass3Seconds = pass3Seconds.total_seconds()
    y = Timer(pass3Seconds, period7)
    y.start()

def period4():
    print("Period 4")
    t_x = datetime.today()
    seconds4 = t_0.replace(day=t_0.day, hour=9, minute=45, second=0, microsecond=0) # Period 4 Ends
    seconds4 = seconds4 - t_x
    seconds4= seconds4.total_seconds()
    if (seconds4 < 0):
        print("Period 4 Already Over!")
    else:
        subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period4Link]))
    x = Timer(seconds4, pass4)
    x.start()

def pass4():
    print("Brunch")
    t_x = datetime.today()
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    subprocess.Popen(pathToZoom)
    pass4Seconds = t_0.replace(day=t_0.day, hour=10, minute=5, second=0, microsecond=0) # Period 5 Starts
    pass4Seconds = pass4Seconds - t_x
    pass4Seconds = pass4Seconds.total_seconds()
    y = Timer(pass4Seconds, period5)
    y.start()

def period5():
    print("Period 5")
    t_x = datetime.today()
    seconds5 = t_0.replace(day=t_0.day, hour=11, minute=20, second=0, microsecond=0) # Period 5 Ends
    seconds5 = seconds5 - t_x
    seconds5 = seconds5.total_seconds()
    if (seconds5 < 0):
        print("Period 5 Already Over!")
    else:
        subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period5Link]))
    x = Timer(seconds5, pass5)
    x.start()

def pass5():
    print("Lunch")
    t_x = datetime.today()
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    subprocess.Popen(pathToZoom)
    pass5Seconds = t_0.replace(day=t_0.day, hour=12, minute=40, second=0, microsecond=0) # Period 6 Starts
    pass5Seconds = pass5Seconds - t_x
    pass5Seconds = pass5Seconds.total_seconds()
    y = Timer(pass5Seconds, period6)
    y.start()

def period6():
    print("Period 6")
    t_x = datetime.today()
    subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period6Link]))
    endDaySeconds = t_0.replace(day=t_0.day, hour=13, minute=55, second=0, microsecond=0) # Period 6 Ends
    endDaySeconds = endDaySeconds - t_x
    endDaySeconds = endDaySeconds.total_seconds()
    y = Timer(endDaySeconds, endDay)
    y.start()

def period7():
    t_x = datetime.today()
    endDaySeconds = t_0.replace(day=t_0.day, hour=15, minute=20, second=0, microsecond=0) # Period 7 Ends
    endDaySeconds = endDaySeconds - t_x
    endDaySeconds = endDaySeconds.total_seconds()
    if (endDaySeconds < 0):
        print("Period 7 Already Over!")
        y = Timer(endDaySeconds, endDay)
        y.start()
    else:
        print("Period 7")
        subprocess.Popen((["C:\Program Files\Google\Chrome\Application\chrome.exe", "-incognito", period7Link]))
        y = Timer(endDaySeconds, endDay)
        y.start()

def endDay():
    print("SchoolDay has Ended, Looping for Tomorrow...")
    subprocess.call(["taskkill", "/F", "/IM", "zoom.exe"])
    t_x = datetime.today()
    t_0 = t_x.replace(day=t_x.day, hour=8, minute=30, second=0, microsecond=0) + timedelta(days=1)
    print(t_0)
    deltaT = t_0 - t_x
    deltaT = deltaT.total_seconds()
    print(deltaT)
    y = Timer(deltaT, period1)
    y.start()

t = Timer(seconds, period1)
t.start()
subprocess.Popen(pathToZoom)
