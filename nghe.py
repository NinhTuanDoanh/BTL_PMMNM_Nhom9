import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:  # dong nay tuong duong voi mic=speech_recognition.Microphone nhung
    print("Robot:I'm listening ")  # khi dung with thi khi nao khong noi thi mic tat con voi mic= thi mic luon luon mo
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you=""
print("You= "+you)
