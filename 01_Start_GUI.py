from tkinter import *


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#CAF0F8") 
        self.start_frame.grid()

        # Mstery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Phobia Quiz",
                                       font="Arial 19 bold", bg="#CAF0F8")
        self.mystery_box_label.grid(row=0)

        # initial instructions (row 1)
        self.mystery_intructions = Label(self.start_frame, font="Arial 10 italic", bg="#CAF0F8",
                                         text="Quiz description does here",
                                         wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_intructions.grid(row=1)

        # Play frame (row 2)
        self.play_frame = Frame(self.start_frame, bg="#CAF0F8")
        self.play_frame.grid(row=2)

        # Play button
        self.play_button = Button(self.play_frame, text="Play",
                                       command=lambda: self.to_game(1),
                                       font="Arial 19", bg="#ADE8F4")
        self.play_button.grid(row=0, column=0, pady=10)


    def to_game(self, stakes):

        Game(self)

        # hide start up window
        root.withdraw()


# Main Routine
if __name__ == "__main__":
    root= Tk() 
    root.title("Phobia Quiz")
    something = Start(root)
    root.mainloop()