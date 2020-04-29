import time
import datetime
starting= input("Hello! Welcome to Typing Time Calculator.\n\nIf you want to stop the program type 'stop' . \n\nType 'start' to start to calculate :")
starting = starting.lower()
if starting == "start" :
    print("Please start to type your text 3 seconds later... ")

    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!!")
    time.sleep(0.1)
    before = datetime.datetime.now()
    text = input("Type here :")
    after = datetime.datetime.now()

    speed = after - before
    seconds = round(speed.total_seconds(),2)
    letter_seconds  = round(len(text)/seconds,1)
    print("Start Time : " , before)
    print("End Time :" , after)
    print("Time to write the text :" , seconds ,"seconds")
    print("SPEED :" , letter_seconds ,"let/sec")

    show_text = input("Type 'yes' to see the text you wrote :")
    if show_text == "yes" :
        print(text)
else :
    print("Seni anlayamıyorum.Doğru yaptığından emin ol.Sistem kapatılıyor...")


