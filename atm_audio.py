from deep_translator import GoogleTranslator
from gtts import gTTS

d={
    "welcome":"Welcome to SBI ATM System",
    "menu":"Press 1.for Sign Up. Press 2 for Sign In. Press 3 for Exit",
    "enter_choice":"Enter your choice ",
    "signup":"Registration Successful",
    "login":"Login Successful"
    }
l={"english":"en","gujarati":"gu","hindi":"hi"}
def audio():
    for i,j in l.items():
        for p,q in d.items():
            if j!="en":
                target_text=GoogleTranslator(source="en",target=j).translate(q)
            else:
                target_text=q

            #generate voice file
            voice=gTTS(text=target_text,lang=j)
            voice.save(f"{p}.mp3")
        print("Audio File is ready")
audio()
print("All files generated")
