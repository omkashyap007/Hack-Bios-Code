import speech_recognition as sr
import pyaudio

# mic = None
for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
    mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=48000)
    print(f"The index is : {i} : {mic}  : {mic_name}")
# mic = sr.Microphone(device_index = 2 , chunk_size = 1024 , sample_rate = 48000)
# print(mic)
pi_ear = sr.Recognizer()
while True : 
    with mic as source : 
        print(f"The software is listening !")
        audio = pi_ear.listen(source)
        print(audio)
    audio = pi_ear.recognize_google(audio)
    print(audio)
pi_ear = sr.Recognizer()
# pi_mouth = GoogleTTS


# while True:
#     need_speak = False
#     with mic as source:
#         audio = pi_ear.listen(source)
#     try:
#         you = pi_ear.recognize_google(audio)
#     except:
#         you = ""
#     msg = you
#     if you == "":
#         msg="I can't hear you, please try again"
#         need_speak = True
#     elif "turn on light" in you:
#         msg="sure, I'm turning on the light"
#         need_speak = True
#     elif "turn on fan" in you:
#         msg="sure, I'm turning on the fan"
#         need_speak = True
#     elif "turn on the light" in you:
#         msg = "sure, I'm turning on the light"
#         need_speak = True
#     elif "turn off light" in you:
#         msg = "sure, I'm turning off the light"
#         need_speak = True
#     elif "turn off fan" in you:
#         msg = "sure, I'm turning off the fan"
#         need_speak = True
#     elif "turn off the light" in you:
#         msg="sure, I'm turning off the light"
#         need_speak = True
#     elif "bye" in you:
#         msg="thank you"
#         print("\033[0;32myou:\033[0m " + you)
#         print("\033[0;35mpi:\033[0m " + msg)
#         pi_mouth.say(msg)
#         pi_mouth.runAndWait()
#         break
#     print("\033[0;32myou:\033[0m " + you)
#     print("\033[0;35mpi:\033[0m " + msg)
#     if need_speak == True:
#         pi_mouth.say(msg)
#         pi_mouth.runAndWait()
