import win32com.client,time

speaker = win32com.client.Dispatch("SAPI.SpVoice");
names=[];
a=int(input("enter the number of names you want to give shoutout : "));
for i in range(a):
    a=i;
    name = input(f"Enter the name of the {a+1} person you want to give shoutout : ");
    names.append(name);

for name in names:
    time.sleep(0.50);
    speaker.Speak(f"shoutout to {name}");
