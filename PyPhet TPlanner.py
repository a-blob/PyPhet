import tkinter
from tkinter import *
from tkinter import ttk
from datetime import date
import datetime
import random

todays_date = date.today()

Font1 = "Arial 11"
Font2 = "Arial 10 bold"


class GUI:
    def __init__(self):
        self.ui = Tk()
        self._setup_main_window()
        self.ui.iconbitmap('./icon.ico')

    def run(self):
        self.ui.mainloop()

    def _setup_main_window(self):

        self.ui.title("PyPhet TPlanner")
        self.ui.resizable(width=False, height=False)
        self.ui.configure(width=475, height=600, bg="#ffffff")

        def copyrightwindow():
            copymsg = tkinter.Tk()
            copymsg.title("Copyright")
            warningmat = tkinter.Label(copymsg, text="This software is licensed under\nthe MIT License\n\n")
            warningmat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(copymsg, text="   Okay   ", command=lambda: copymsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            copymsg.resizable(False, False)
            copymsg.iconbitmap('./icon.ico')

        def quit_destroy():
            self.ui.destroy()

        # Define About Window
        def aboutwndow():
            aboutmsg = tkinter.Tk()
            aboutmsg.title("About")
            warningmat = tkinter.Label(aboutmsg, text="You can use this to plan recent things.")
            warningmat.pack(side="top", fill="both", expand=False, padx=100, pady=40)
            button = ttk.Button(aboutmsg, text="   Okay   ", command=lambda: aboutmsg.destroy())
            button.pack(side="bottom", fill="none", expand=True)
            aboutmsg.resizable(False, False)
            aboutmsg.iconbitmap('./icon.ico')

        main_menu = Menu(self.ui)

        file_menu = Menu(self.ui)
        help_menu = Menu(self.ui)

        main_menu.add_cascade(label="PyPhet", menu=file_menu)
        file_menu.add_command(label='Quit', command=quit_destroy)

        main_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=aboutwndow)
        help_menu.add_command(label="Copyright", command=copyrightwindow)

        self.ui.config(menu=main_menu)

        # Add Label
        head_label = Label(self.ui, bg="#f1f1f1", fg="#4c4c4c",
                           text='Ask a "When?" Question Below', font=Font2, pady=11)
        head_label.place(relwidth=1)

        # Add Divider
        line = ttk.Label(self.ui, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Add Container
        self.text_widget = Text(self.ui, width=20, height=2, bg="#f1f1f1", fg="#656565",
                                font=Font1, padx=5, pady=5)
        self.text_widget.place(relheight=0.845, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Add Scroll Bar
        scrollbar = ttk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label = Label(self.ui, bg="#e6e5e5", height=60)
        bottom_label.place(relwidth=1, rely=0.925)

        # Add Entry
        self.msg_entry = ttk.Entry(bottom_label, font=Font1)
        self.msg_entry.place(relwidth=0.74, relheight=0.025, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.enter_press)

        # Add Button
        send_button = ttk.Button(bottom_label, text="Send", width=20,
                                 command=lambda: self.enter_press(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.025, relwidth=0.22)

    # Add Ability to Send Text When You Press Enter 
    def enter_press(self, event):
        msg = self.msg_entry.get()
        self.display_message(msg, "You")

    def display_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:  {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        now = datetime.datetime.now()
        determer = now.strftime("%H")
        p_date = ""
        timeh = ""
        abt = int(determer)
        dated = random.randrange(1, 4)
        if dated == 1:
            p_date = "today"
            timeh = random.randrange(abt, 24)
        if dated == 2:
            p_date = "tommorow"
            timeh = random.randrange(5, 24)
        if dated == 3:
            p_date = "the day after tommorow"
            timeh = random.randrange(5, 24)

        times = random.randrange(0, 60)

        msg2 = f"PyPhet:  on {p_date}, {timeh}:{times} \n\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


def warning():
    msg = tkinter.Tk()
    msg.title("Disclaimer Message")
    warningmat = tkinter.Label(msg, text='''
    Statement: If something happens to\n you in real life because of this software, \n
    the creators of this software\n will not be responsible!\n\n
    By either clicking 'Okay' or closing this window, \nyou agree to the statement above.
    ''')
    warningmat.pack(side="top", fill="both", expand=False, padx=90, pady=30)
    button = ttk.Button(msg, text="   Okay   ", command=lambda: msg.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    msg.resizable(False, False)
    msg.iconbitmap('./icon.ico')
    msg.mainloop()


if __name__ == "__main__":
    warning()

    app = GUI()
    app.run()
