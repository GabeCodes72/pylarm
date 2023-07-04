import datetime, winsound, threading
import datetime

print("When do you want your alarm to go off? ")

start = datetime.time(*[int(x) for x in input('Insert your time. (24 Hour Format (Hour:Minute))\n > ').split(':')])
end = datetime.time(*[int(x) for x in input("If you don't turn it off when it goes off, when do you want it to stop? (24 Hour Format(Hour:Minute))\n > ").split(':')])
noise = input("""
What noise do you want to play?
1. Calendar Alert
2. Email Alert
3. Tada
4. Battery Alert
5. Error
6. Alarm
7. Windows Problem
> """)
if noise == "1":
    alarmNoise = "sounds/Windows Notify Calendar.wav"
elif noise == "2":
    alarmNoise = "sounds/Windows Notify Email.wav"
elif noise == "3":
    alarmNoise = "sounds/tada.wav"
elif noise == "4":
    alarmNoise = "sounds/Windows Battery Low.wav"
elif noise == "5":
    alarmNoise = "sounds/Windows Critical Stop.wav"
elif noise == "6":
    alrmChoice = input("""
Which alarm?
1. Alarm01
2. Alarm02
3. Alarm03
4. Alarm04
5. Alarm05
6. Alarm06
7. Alarm07
8. Alarm08
9. Alarm09
10. Alarm10
> """)
    if alrmChoice == "1":
        alarmNoise = "sounds/Alarm01.wav"
    if alrmChoice == "2":
        alarmNoise = "sounds/Alarm02.wav"
    if alrmChoice == "3":
        alarmNoise = "sounds/Alarm03.wav"
    if alrmChoice == "4":
        alarmNoise = "sounds/Alarm04.wav"
    if alrmChoice == "5":
        alarmNoise = "sounds/Alarm05.wav"
    if alrmChoice == "6":
        alarmNoise = "sounds/Alarm06.wav"
    if alrmChoice == "7":
        alarmNoise = "sounds/Alarm07.wav"
    if alrmChoice == "8":
        alarmNoise = "sounds/Alarm08.wav"
    if alrmChoice == "9":
        alarmNoise = "sounds/Alarm09.wav"
    if alrmChoice == "10":
        alarmNoise = "sounds/Alarm10.wav"
elif noise == "7":
    alarmNoise = "sounds/fish.wav"
while True:
    now = datetime.datetime.now().time()
    if start <= now <= end:
        t = threading.Thread(target=winsound.PlaySound, args=[alarmNoise, winsound.SND_FILENAME])
        t.start()
        t.join()
