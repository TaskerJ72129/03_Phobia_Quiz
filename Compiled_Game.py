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

class Game:
    def __init__(self,partner):
        
        # GUI Setup
        self.game_box = Toplevel()

        # If users press cross at top, game quits
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Phobia Quiz",
                                   font="Arial 24 bold", padx=10, pady=10, bg="#CAF0F8")
        self.heading_label.grid(row=0)

        # Question number Label
        self.question_number_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Question number goes here",
                                        font="Arial 10", padx=10, pady=10, bg="#CAF0F8")
        self.question_number_label.grid(row=1)
        
        # Boxes go here (row 2)
        self.box_frame = Frame(self.game_frame, bg="#CAF0F8")
        self.box_frame.grid(row=2, pady=10)

        
        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#CAF0F8",
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=self.reveal_boxes)

    
        # Help and Game Stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                  font="Arial 14 bold", bg="#808080", fg="white",
                                  command=self.to_help)
        self.help_button.grid(row=0, column=1, padx=2)

        # Stats button
        self.stats_button = Button(self.help_export_frame, text="Game Stats", font=("Arial 14 bold"),
                                   bg="blue", fg="white", 
                                   command=lambda: self.to_stats(self.round_stats_list, self.game_stats_list))
        self.stats_button.grid(row=0, column=2, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)
        
    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)



        



# Main Routine
if __name__ == "__main__":
    root= Tk() 
    root.title("Phobia Quiz")
    something = Start(root)
    root.mainloop()