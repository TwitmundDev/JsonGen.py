import tkMessageBox
from Tkinter import *
import os


def MessageBoxInf():
    label = "SIKE"
    message="SIKE TOO "
    top = Tk()
    top.geometry("1x1")
    tkMessageBox.showinfo("SIKE", "SIKE TOO ")

    top.withdraw()



def CreateDir(name_1,pdir_1,name_2,pdir_2):

    # Path
    path = os.path.join(pdir_1, name_1)

    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    try:
        os.mkdir(path)
        print("Directory '% s' created" % name_1)
    except WindowsError as e :
        if e.winerror == 183:
            print('Dossier deja existant ')

    mode = 0o666

    # Path
    path = os.path.join(pdir_2, name_2)

    try:
        os.mkdir(path)
        print("Directory '% s' created" % name_2)
    except WindowsError as e :
        if e.winerror == 183:
            print('Dossier deja existant ')


def CreateDir1_8_9():
    return CreateDir(name_1="Test",name_2="Test2",pdir_1="C:\Users\twitm\Desktop",pdir_2="C:\Users\twitm\Desktop")


def PrintDesktop():

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    print("The Desktop path is: " + desktop)



#Others app
def App_1_8_9():
    bg_colors='#808080'

    window_1_8_9 = Tk()
    window_1_8_9.title('1.8.9 module')

    FrameQuit = Frame(window_1_8_9,bg=bg_colors)
    FrameQuit.pack(side=BOTTOM)

    window_1_8_9.geometry('720x480')
    window_1_8_9.minsize(480, 360)
    window_1_8_9.config(background=bg_colors)

    label_title = Label(window_1_8_9, background=bg_colors, fg="white", text="1.8.9 module", font=("Courrier", 40))
    label_title.pack()

    makedir= Button(window_1_8_9,
                    text='Make dir',
                    bg=bg_colors,
                    font=('Courrier',25),
                    command= MessageBoxInf
                    ).pack()


    quit = Button(FrameQuit,text='Quit',fg="red",bg=bg_colors,font=('Courrier',15),command=window_1_8_9.destroy).pack()




    window_1_8_9.mainloop()




def App_1_9_4():
    bg_colors='#808080'

    window_1_9_4 = Tk()
    window_1_9_4.title('1.9.4 module')

    FrameQuit = Frame(window_1_9_4,bg=bg_colors)
    FrameQuit.pack(side=BOTTOM)

    window_1_9_4.geometry('720x480')
    window_1_9_4.minsize(480, 360)
    window_1_9_4.config(background=bg_colors)

    label_title = Label(window_1_9_4, background=bg_colors, fg="white", text="1.9.4 module", font=("Courrier", 40))
    label_title.pack()


    quit = Button(FrameQuit,text='Quit',fg="red",bg=bg_colors,font=('Courrier',15),command=window_1_9_4.destroy).pack()




    window_1_9_4.mainloop()


#Main App
def MainApp():
    bg_colors='#808080'

    window = Tk()
    window.title('Hello')

    window.geometry('720x480')
    window.minsize(480, 360)
    window.config(background=bg_colors)

    frame= Frame(window, bg=bg_colors)



    label_title = Label(window,background=bg_colors,fg="white" ,text="Hello world", font=("Courrier", 40))
    label_title.pack()

    JsonB_1_8_9 = Button(frame,text='1.8.9 Menu', bg=bg_colors, fg='white', font=('Courrier', 25),command=App_1_8_9)
    JsonB_1_8_9.pack(pady=5, fill=X)

    JsonB_1_9_4 = Button(frame,text='1.9.4 Menu', bg=bg_colors, fg='white', font=('Courrier', 25),command=App_1_9_4)
    JsonB_1_9_4.pack(pady=5, fill=X)

    frame.pack(expand=YES)


    window.mainloop()



if __name__ =='__main__':
    def Start():
        MainApp()


    Start()