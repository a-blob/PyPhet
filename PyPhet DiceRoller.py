from tkinter import *
from tkinter import ttk
import random
import tkinter

Font1 = "Arial 11"
Font2 = "Arial 10 bold"


class GUI:
    def __init__(self):
        self.ui = Tk()
        self._setup_main_window()
        self.ui.iconbitmap('./icon.ico')
        self.pyphet_sentence_variants = ["the result is", "I rolled a", "looks like it is a",
                                         "the dice landed on", "it is a", "the dice rolled on", "just a",
                                         "just a simple",
                                         "cool, a", "that's a", "ohhhhhhhhhhh,"]

    def run(self):
        self.ui.mainloop()

    def _setup_main_window(self):
        self.ui.title("PyPhet DiceRoller")
        self.ui.resizable(width=False, height=False)
        self.ui.configure(width=600, height=375, bg="#ffffff")

        def copyrightwindow():
            copymsg = tkinter.Tk()
            copymsg.title("Copyright")
            warningmat = tkinter.Label(copymsg, text="This software is licensed under the\n MIT license because it is "
                                                     "complete trash")
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
            warningmat = tkinter.Label(aboutmsg, text="Use this to flip coins")
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
                           text="Dice Result", font=Font2, pady=2)
        head_label.place(relwidth=0.67)

        # Add Divider
        line = ttk.Label(self.ui, width=450)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Add Container
        self.text_widget = Text(self.ui, width=20, height=2, bg="#f1f1f1", fg="#656565",
                                font=Font1, padx=5, pady=5)
        self.text_widget.place(relheight=0.930, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Add Scroll Bar
        scrollbar = ttk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Add Holder
        bottom_label = Label(self.ui, bg="#e6e5e5", height=60)
        bottom_label.place(relwidth=1, x=400, y=0)

        # Add Button
        send_button = ttk.Button(bottom_label, text="Roll A Dice", width=30,
                                 command=lambda: self.roll1(None))
        send_button.place(relx=-0.01, rely=-0.01, relheight=0.22, relwidth=0.35)

        # Button
        send_button = ttk.Button(bottom_label, text="Roll Two Dice", width=30,
                                 command=lambda: self.roll2(None))
        send_button.place(relx=-0.01, rely=0.2, relheight=0.22, relwidth=0.35)

    def roll1(self, msg):
        dice = random.randrange(1, 7)
        pyphet_sentence = random.choice(self.pyphet_sentence_variants)

        msg2 = f"PyPhet:   {pyphet_sentence} {dice} \n\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def roll2(self, msg):
        # Determ What PyPhet Should Say
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        main = dice1 + dice2
        pyphet_sentence = random.choice(self.pyphet_sentence_variants)

        msg2 = f"PyPhet:   {pyphet_sentence} {dice1} and a {dice2} ({main}) \n\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = GUI()
    app.run()
