user1 = [['09:30','10:00'],['12:30','13:30'],['15:30','16:30']]
user2 = [['10:30','11:00'],['14:30','16:30']]
userstart = ['09:00','17:00']

def truetime(time):
    hour = int(time[0:2])
    minute = int(time[3:5])
    return (hour*60)+minute

def reverse_truetime(time):
    minute = time % 60
    hour = int((time - minute) / 60)
    newtime = str(hour) + ':' + str(minute)
    return newtime

def busytimes(user):
    busytimes = []
    for meeting in user:
        start_meeting = truetime(meeting[0])
        end_meeting = truetime(meeting[1])
        t = start_meeting
        while t < end_meeting:
            busytimes.append(t)
            t+=1
    return busytimes

def createtimetable():
    timetable = []
    starttime = truetime(userstart[0])
    endtime = truetime(userstart[1])
    t = starttime
    while t < endtime:
        timetable.append(t)
        t=t+1
    return timetable
            
timetable = createtimetable()

for time in busytimes(user1):
    if time in timetable:
        timetable.remove(time)
for time in busytimes(user2):
    if time in timetable:
        timetable.remove(time)
        

freetimes = []
run = False
for time in timetable:
    if run == False:
        prevtime = time - 1
        startrun = time
    run = True
    if time != prevtime + 1:
        endrun = prevtime
        freetimes.append([reverse_truetime(startrun),reverse_truetime(endrun)])
        run = False
    prevtime = time       

print(freetimes)