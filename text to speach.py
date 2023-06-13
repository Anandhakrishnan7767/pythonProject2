from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

# text='today is good'
# output=gTTS(text=text,lang='en',slow=False)
# output.save('output.mp3')
# os.system('start output.mp3')


# file data to audio
# text=open('demo','r').read()
# language = 'hi'
# output=gTTS(text=text ,lang='en',slow=False)
# output.save('output.mp3')
# os.system('start output.mp3')


# useer input

def texttospeach():
    text=entery.get()
    output=gTTS(text=text,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')
entery=Entry(root)
canvas.create_window(200,180,window=entery)
button=Button(text='start',command=texttospeach)
canvas.create_window(200,300,window=button)
root.mainloop()


