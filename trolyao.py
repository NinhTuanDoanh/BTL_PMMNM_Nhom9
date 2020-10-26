import speech_recognition
import pyttsx3
from datetime import date ,datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""

while True:
    with speech_recognition.Microphone() as mic:  # dong nay tuong duong voi mic=speech_recognition.Microphone nhung
        print("Robot:I'm listening ")  # khi dung with thi khi nao khong noi thi mic tat con voi mic= thi mic luon luon mo
        audio = robot_ear.listen(mic)
    print("Robot:...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you=""
    print("You= "+you)

    if you=="":
        robot_brain="I can't hear you,try again!"
    elif "hello" in you:
        robot_brain="Hello how can i help you"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime(" now is: %H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain="The president of American is DonalTrump"
    elif "bye" in you:
        robot_brain="Bye see you again"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain="I'm fine thanks and you!"
    print(robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()