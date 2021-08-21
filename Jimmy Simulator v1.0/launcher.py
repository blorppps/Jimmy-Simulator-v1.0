from tkinter import *

#launcher setup
'START BLOCK'
window = Tk()
window.title('Jimmy Simulator')

def end():
    global cheats
    global horror
    global music
    
    cheats = cheats.get()
    horror = horror.get()
    music = music.get()

    window.destroy()

label = Label(window,text='Jimmy Simulator')
cheats = IntVar()
horror = IntVar()
music = IntVar()
check1 = Checkbutton(window,text='Cheats',onvalue=1,offvalue=0,variable=cheats)
check2 = Checkbutton(window,text='Non-Horror Mode',onvalue=1,offvalue=0,variable=horror)
check3 = Checkbutton(window,text='Music',onvalue=1,offvalue=0,variable=music)
button = Button(window,text='Play',command=end)
'END BLOCK'

#draws launcher
'START BLOCK'
window.geometry('150x130')
label.pack()
check1.pack()
check2.pack()
check3.pack()
button.pack()

window.mainloop()
'END BLOCK'
