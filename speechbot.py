import speech_recognition as sr
import tkinter as tk

def texttt():
        filename = ent.get().strip('"') 
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
           audio_data = r.record(source)
           textt = r.recognize_google(audio_data)
           print(textt)
           labb.config(text=textt)

root = tk.Tk()
head=tk.Label(text="SPEECHBOT",bg='gray',width=200,height=5,font=("Helvetica",16),fg="white")
head.pack()
lab = tk.Label(root, text="Enter File Path here", width=200)  # Setting width to 200 pixels
lab.pack()
ent = tk.Entry(root, width=100,bg="blue",fg="white",text="Enter File Path")  # Setting width to 100 characters
ent.pack()
button = tk.Button(root, text="Get Speech", command=lambda: texttt(), width=85)  # Setting width to 20 characters
button.pack()
labb = tk.Label(root)
labb.pack()

root.mainloop()
