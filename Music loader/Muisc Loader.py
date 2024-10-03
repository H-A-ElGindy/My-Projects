from pygame import mixer
from tkinter import *
from tkinter import filedialog

class Player:
    def __init__(self,window):
        
        window.geometry('320x100');window.title('Python Player');window.resizable(0,0)
        Load=Button(window, text = "Load", width=10, font=('Times', 10), command=self.load)
        Play=Button(window, text = "Play", width=10, font=('Times', 10), command=self.play)
        global Pause
        Pause=Button(window, text = "Pause", width=10, font=('Times', 10), command=self.pause)
        Stop=Button(window, text = "Stop", width=10, font=('Times', 10), command=self.stop)
        Load.place(x=0,y=20); Play.place(x=110,y=20); Pause.place(x=220,y=20); Stop.place(x=110,y=60)
        self.music_file=False 
        self.play_state=False    
    def load(self):
        self.music_file=filedialog.askopenfilename()   
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()        
    def pause(self):
        if not self.play_state:
            Pause=Button(text = "Resume", width=10, font=('Times', 10), command=self.pause)
            Pause.place(x=220,y=20)
            mixer.music.pause()
            self.play_state=True
        else:
            Pause=Button(text = "Pause", width=10, font=('Times', 10), command=self.pause)
            Pause.place(x=220,y=20)
            mixer.music.unpause()
            self.play_state=False   
    def stop(self):
        mixer.music.stop()

new_root=Tk()
player_app=Player(new_root)
new_root.mainloop()