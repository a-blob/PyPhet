# Display Terminal Message
print("Not a developer? Please minimize this window.\n\n")



# Import UI Add-on
from tkinter import *
from tkinter import ttk
print("Imported Tkinter")



# Import Webbrowser Add-on
import webbrowser
print("Imported Webbrowser")



# Import the Ability to Wait
import time
print("Imported Time")



# Import Random Number Generator
import random
print("Imported Random")
import tkinter
print("Imported Tkinter")



# Define Fonts
Font1 = "Arial 11"
Font2 = "Arial 10 bold"
print("Fonts Defined")



# Define User Interface
class GUI:
    


    # Creat Window
    def __init__(self):
        self.ui = Tk()
        self._setup_main_window()
        self.ui.iconbitmap('.\icon.ico')
        

    # Creat UI Loop    
    def run(self):
        self.ui.mainloop()



    # Filling Up Window With Details    
    def _setup_main_window(self):
        
        

        # Customize Window Size & Functions
        self.ui.title("PyPhet Questioner")
        self.ui.resizable(width=False, height=False)
        self.ui.configure(width=475, height=600, bg="#ffffff")



        # Define About MSG (Message Box)
        def CreditsWindow():
            creditmsg = tkinter.Tk()
            creditmsg.title("Credits")
            warningMat = tkinter.Label(creditmsg, text="Made by a-blob \n https://github.com/a-blob \n\n")
            warningMat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(creditmsg, text="   Okay   ", command=lambda: creditmsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            creditmsg.resizable(False, False)
            msg.iconbitmap('.\icon.ico')
            creditmsg.mainloop
            print("Credits Window Displayed\n")

        
        # Define Copyright MSG (Message Box)
        def CopyrightWindow():
            copymsg = tkinter.Tk()
            copymsg.title("Copyright")
            warningMat = tkinter.Label(copymsg, text="This software is licensed under\n" 
                "the MIT License\n\n" 
                "Go to this website for more information:\n"
                "https://mit-license.org/")
            warningMat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(copymsg, text="   Okay   ", command=lambda: copymsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            copymsg.resizable(False, False)
            msg.iconbitmap('.\icon.ico')
            copymsg.mainloop
            print("Copyright Window Displayed\n")

    

        # Define Quit Command
        def quit_destroy():
            self.ui.destroy()

        

        # Define Version Window (Message Box)
        def VersionWindow():
            versionmsg = tkinter.Tk()
            versionmsg.title("Version")
            warningMat = tkinter.Label(versionmsg, text="PyPhet\n" 
                "App: Questioner\n\n"
                "Version: 1.1")
            warningMat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(versionmsg, text="   Okay   ", command=lambda: versionmsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            versionmsg.resizable(False, False)
            msg.iconbitmap('.\icon.ico')
            versionmsg.mainloop
            print("Version Window Displayed\n")



        # Define About Window
        def AboutWndow():
            aboutmsg = tkinter.Tk()
            aboutmsg.title("About")
            warningMat = tkinter.Label(aboutmsg, text="PyPhet\n" 
                "App: Questioner\n"
                "PyPhet Questioner is a simple software programed with Python\n"
                "that answers your Yes or No questions. You can ask it questions\n"
                "so it can help you determine what to do in yout real life situations.\n"
                "This software is helpful when it comes to making decisions.\n")
            warningMat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(aboutmsg, text="   Okay   ", command=lambda: aboutmsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            aboutmsg.resizable(False, False)
            msg.iconbitmap('.\icon.ico')
            aboutmsg.mainloop
            print("About Window Displayed\n")


        # Define Website Opener
        def OpenWeb():
            webbrowser.open("https://github.com/a-blob/PyPhet")
            print("Browser Opened")



        # Define Website Opener2
        def OpenWe2b():
            webbrowser.open("https://github.com/a-blob/PyPhet")
            print("Browser Oppened")


        
        # Define Update Window
        def Updatewindow():
            updatemsg = tkinter.Tk()
            updatemsg.title("Update")
            warningMat = tkinter.Label(updatemsg, text=
                "You are currently using PyPhet version 1.1\n\n"
                "Click Check For Updates to check for updates\n")
            warningMat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            butto2 = ttk.Button(updatemsg, text="   Check For Updates   ", command=OpenWe2b)
            butto2.pack(side="bottom", fill="none", expand=True)
            updatemsg.resizable(False, False)
            msg.iconbitmap('.\icon.ico')
            updatemsg.mainloop
            print("Help Window Displayed\n")



        # Add Top Menu
        main_menu = Menu(self.ui)

        file_menu = Menu(self.ui)
        edit_menu = Menu(self.ui)
        help_menu = Menu(self.ui)
        
        main_menu.add_cascade(label="PyPhet", menu = file_menu)
        file_menu.add_command(label = "Website", command=OpenWeb)
        file_menu.add_command(label = "Version", command=VersionWindow)
        file_menu.add_command(label='Quit', command=quit_destroy)

        main_menu.add_cascade(label="Another dropdown because why not?", menu = edit_menu)
        edit_menu.add_command(label = "Update", command=Updatewindow)
        edit_menu.add_command(label='Credits', command=CreditsWindow)

        main_menu.add_cascade(label="Help", menu = help_menu)
        help_menu.add_command(label = "About", command= AboutWndow)
        help_menu.add_command(label = "Copyright", command=CopyrightWindow)
        
        self.ui.config(menu=main_menu)



        # Add Instruction Label
        head_label = Label(self.ui, bg="#f1f1f1", fg="#4c4c4c",
                           text="Ask a Yes or No Question Below", font=Font2, pady=11)
        head_label.place(relwidth=1)
        
        

        # Add Divider Below Instruction Label
        line = ttk.Label(self.ui, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        

        # Add Chat History Container
        self.text_widget = Text(self.ui, width=20, height=2, bg="#f1f1f1", fg="#656565",
                                font=Font1, padx=5, pady=5)
        self.text_widget.place(relheight=0.845, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        

        # Add Chat History Container Scroll Bar
        scrollbar = ttk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        

        # Add Message Enter Box Holder
        bottom_label = Label(self.ui, bg="#e6e5e5", height=60)
        bottom_label.place(relwidth=1, rely=0.925)
        

        
        # Add Message Enter Box
        self.msg_entry = ttk.Entry(bottom_label, font=Font1)
        self.msg_entry.place(relwidth=0.74, relheight=0.025, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.enter_press)
        
        

        # Add "Send" Button
        send_button = ttk.Button(bottom_label, text="Send", width=20, 
                             command=lambda: self.enter_press(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.025, relwidth=0.22)

    

    # Add Ability to Send Text When You Press Enter 
    def enter_press(self, event):
        msg = self.msg_entry.get()
        self.display_message(msg, "You")
        print("PyPhet Message Displayed\n")
        
    

    # Define Chat Display Functions
    def display_message(self, msg, sender):
        if not msg:
            return
        


        # Display User's Message On Chat History Box
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:  {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        


        # Determ What PyPhet Should Say
        determ = random.randrange(1, 11)
        print ("OUTPUT determ = ", determ, "\n")
        if determ == 1:
            PyPhet_Answer = "yes"
        if determ == 2:
            PyPhet_Answer = "definitely"
        if determ == 3:
            PyPhet_Answer = "my answer is yes"
        if determ == 4:
            PyPhet_Answer = "ofcourse"
        if determ == 5:
            PyPhet_Answer = "it's certain"
        if determ == 6:
            PyPhet_Answer = "no"
        if determ == 7:
            PyPhet_Answer = "the answer is no"
        if determ == 8:
            PyPhet_Answer = "I would say no"
        if determ == 9:
            PyPhet_Answer = "not likely"
        if determ == 10:
            PyPhet_Answer = "certainly not"
        else:
            pass
        
        

        # Display Pyphet's Message On The Message History Box
        msg2 = "PyPhet:   " + PyPhet_Answer + "\n\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        print("Self Message Displayed")
    
        self.text_widget.see(END)



        # Give PyPhet Some (Fake) Time To Think (LOL)
        time.sleep(0.5)



# Print Debug Info
print("Window + Details Created\n")    
print("Displaying Warning")  



# Define Warning MSG (Message Box)
def Warning():
    msg = tkinter.Tk()
    msg.title("Disclaimer Message")
    warningMat = tkinter.Label(msg, text="" 
        "Statement: If something happens to\n you in real-life because of this software, \n"
        "the creators of this software\n will not be responsible!\n\n"
        "By either clicking 'Okay' or closing this window, \nyou agree to the statement above.")
    warningMat.pack(side="top", fill="both", expand=False, padx=90, pady=30)
    button = ttk.Button(msg, text="   Okay   ", command=lambda: msg.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    msg.resizable(False, False)
    msg.iconbitmap('.\icon.ico')
    msg.mainloop()
    
    print("Warning Closed\n")
    print("Main Window Starting\n")
        
        

# Display All Defined Settings        
if __name__ == "__main__": 
    Warning()
    
    app = GUI()
    app.run()
