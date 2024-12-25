import time

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice");
shell = win32com.client.Dispatch("WScript.Shell")

for i in range(100):
    speaker.Speak("Drink water");
    shell.Popup("its been two hours you should drink water", 0, "Message Title", 64)
    time.sleep(7200);



