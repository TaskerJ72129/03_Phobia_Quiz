from tkinter import *
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#CAF0F8") 
        self.start_frame.grid()

        # Mstery Heading (row 0)
        self.start_label = Label(self.start_frame, text="Phobia Quiz",
                                       font="Arial 19 bold", bg="#CAF0F8")
        self.start_label.grid(row=0)

        # initial instructions (row 1)
        self.quiz_intructions = Label(self.start_frame, font="Arial 10 italic", bg="#CAF0F8",
                                         text="This is a quiz where you get given a question asking what a certain phobia is the fear of and you get given 4 multiple choice answers to choose from."
                                              "There are 113 Phobias in this quiz shown in a random order but you can check your stats and quit at any point",
                                         wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_intructions.grid(row=1)

        # Play frame (row 2)
        self.play_frame = Frame(self.start_frame, bg="#CAF0F8")
        self.play_frame.grid(row=2)

        # Play button
        self.play_button = Button(self.play_frame, text="Play",
                                       command=lambda: self.to_quiz(),
                                       font="Arial 19", bg="#ADE8F4")
        self.play_button.grid(row=0, column=0, pady=10)


    def to_quiz(self):

        Quiz(self)

        # hide start up window
        root.withdraw()

class Quiz:
    def __init__(self,partner):

    

        self.phobia_list = ['Achluophobia ', 'Acousticophobia ', 'Acrophobia ', 'Aerophobia ', 'Agoraphobia ', 'Agyrophobia ', 'Aichmophobia ', 'Ailurophobia ', 'Algophobia ', 'Ancraophobia ', 
        'Aquaphobia ', 'Arachnophobia ', 'Astraphobia ', 'Autophobia ', 'Bacteriophobia ', 'Basophobia ', 'Batrachophobia ', 'Belonephobia ', 'Bibliophobia ', 'Cacophobia ', 'Carcinophobia ', 
        'Catoptrophobia ', 'Chemophobia ', 'Cherophobia ', 'Chiroptophobia ', 'Chromophobia ', 'Chronomentrophobia ', 'Chronophobia ', 'Cibophobia ', 'Claustrophobia ', 'Coimetrophobia ', 
        'Coulrophobia ', 'Cyberphobia ', 'Cynophobia ', 'Demonophobia ', 'Dendrophobia ', 'Dentophobia ', 'Domatophobia ', 'Emetophobia ', 'Enochlophobia ', 'Entomophobia ', 'Ephebiphobia ', 
        'Equinophobia ', 'Ergophobia ', 'Frigophobia ', 'Gamophobia ', 'Gephyrophobia ', 'Gerascophobia ', 'Germophobia ', 'Globophobia ', 'Glossophobia ', 'Halitophobia ', 'Heliophobia ', 
        'Helminthophobia ', 'Hemophobia ', 'Herpetophobia ', 'Hexakosioihexekontahexaphobia ', 'Hodophobia ', 'Hydrophobia ', 'Hypochondria ', 'Ichthyophobia ', 'Insectophobia ', 'Koumpounophobia ', 
        'Lepidopterophobia ', 'Lilapsophobia ', 'Mageirocophobia ', 'Melanophobia ', 'Melissophobia ', 'Monophobia ', 'Musophobia ', 'Myrmecophobia ', 'Necrophobia ', 'Neophobia ', 'Noctiphobia ', 
        'Nosocomephobia ', 'Numerophobia ', 'Nyctophobia ', 'Obesophobia ', 'Ommetaphobia ', 'Oneirophobia ', 'Ophidiophobia ', 'Ornithophobia ', 'Osmophobia ', 'Ostraconophobia ', 'Panphobia ', 
        'pediaphobia ', 'Pharmacophobia ', 'Phasmophobia ', 'Phobophobia ', 'Phonophobia ', 'Pogonophobia ', 'Porphyrophobia ', 'Pteromerhanophobia ', 'Pyrophobia ', 'Radiophobia ', 
        'Siderodromophobia ', 'Sociophobia ', 'Somniphobia ', 'Taphophobia ', 'Technophobia ', 'Tetraphobia ', 'Thalassophobia ', 'Thanatophobia ', 'Thermophobia ', 
        'Toxiphobia ', 'Traumatophobia ', 'Trichophobia ', 'Triskaidekaphobia ','Vehophobia ', 'Xanthophobia ', 'Xenophobia '
        ]

        self.fear_name_list = ['darkness', 'noise', 'heights', 'flying', 'open spaces', 'crossing streets', 'sharp objects', 'cats', 'pain', 'wind', 'water', 'spiders', 'thunder and lightning',
        'isolation', 'bacteria', 'falling', 'frogs', 'needles', 'books', 'ugliness', 'cancer', 'mirrors', 'chemicals', 'happiness', 'bats', 'colours', 'clocks', 'time passing', 'food', 
        'closed spaces', 'cemetries', 'clowns', 'computers', 'dogs', 'demons', 'trees', 'dentists', 'houses', 'vomiting', 'crowds', 'insects', 'youth', 'horses', 'work', 'cold', 'marriage', 
        'bridges', 'aging', 'germs', 'balloons', 'public speaking', 'bad breath', 'sunlight', 'worms', 'blood', 'reptiles', '666', 'travel', 'water', 'illness', 'fish', 'insects', 'buttons', 
        'butterflies', 'tornadoes or hurricanes', 'cooking', 'black', 'bees', 'being alone', 'mice', 'ants', 'death', 'new things', 'night', 'hospitals', 'numbers', 'darkness', 
        'weight gain', 'eyes', 'dreams', 'snakes', 'birds', 'smells', 'shellfish', 'everything', 'babies and children', 'medicine', 'ghosts', 'fear', 'loud sounds', 'beards', 'purple', 
        'flying', 'fire', 'radioactivity', 'trains', 'people', 'sleep', 'graves', 'technology', '4', 'sea', 'dying', 'heat', 'poisons', 'injury', 'hair loss', '13', 
        'driving', 'yellow', 'foreigners'
        ]

        
        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.quiz_frame = Frame(self.quiz_box, bg="#F8F9FA")
        self.quiz_frame.grid()

        # Heading Row
        self.heading_label = Label(self.quiz_frame, text="Phobia Quiz",
                                   font="Arial 24 bold", padx=10, pady=10, bg="#F8F9FA")
        self.heading_label.grid(row=0)

        self.round_num = 0
        print(self.round_num)

        

        # Question number Label
        self.question_number_label = Label(self.quiz_frame, wrap=300, justify=LEFT,
                                        text="question number",
                                        font="Arial 10", padx=10, pady=10, bg="#F8F9FA")
        self.question_number_label.grid(row=1)

        # Question Label
        self.question_label = Label(self.quiz_frame, wrap=600, justify=LEFT,
                                        text="Question goes here",
                                        font="Arial 16", padx=10, pady=10, bg="#F8F9FA")
        self.question_label.grid(row=2)

        answer1 = "answer 1"
        answer2 = "answer 2"

        # Answer buttons go here (row 3)
        self.box_frame = Frame(self.quiz_frame, bg="#F8F9FA")
        self.box_frame.grid(row=3, pady=10)

        self.answer_button_1 = Button(self.box_frame, text=answer1, bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10)
        self.answer_button_1.grid(row=0, column=1, padx=2, pady=2)


        self.answer_button_2 = Button(self.box_frame, text=answer2, bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10)
        self.answer_button_2.grid(row=0, column=2, padx=2, pady=2)


        self.answer_button_3 = Button(self.box_frame, text="Answer Buttons", bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10)
        self.answer_button_3.grid(row=1, column=1, padx=2, pady=2)

        self.answer_button_4 = Button(self.box_frame, text="Answer Buttons", bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10)
        self.answer_button_4.grid(row=1, column=2, padx=2, pady=2)


        # Next Question Button (row 5)
        self.next_button_frame = Frame(self.quiz_frame, bg="#F8F9FA")
        self.next_button_frame.grid(row=5, pady=10)

        self.next_button = Button(self.next_button_frame, text="Next Question", font=("Arial 14 bold"),
                                   bg="#CED4DA", 
                                   command=self.question_and_answers)
        self.next_button.grid(row=0, column=2, padx=2)

        # self.next_button.config(state=DISABLED)
    
        # Help and Quiz Stats button (row 6)
        self.help_export_frame = Frame(self.quiz_frame, bg="#F8F9FA")
        self.help_export_frame.grid(row=6, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                  font="Arial 14 bold", bg="#CED4DA",
                                  command=self.to_help)
        self.help_button.grid(row=0, column=1, padx=2)

        # Stats button
        self.stats_button = Button(self.help_export_frame, text="Stats", font=("Arial 14 bold"),
                                   bg="#CED4DA", 
                                   command=lambda: self.to_stats(self.round_stats_list, self.quiz_stats_list))
        self.stats_button.grid(row=0, column=2, padx=2)

        # Quit Button
        self.quit_button = Button(self.quiz_frame, text="Quit",
                                  bg="#343a40", fg="white", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=7, pady=10)

        self.question_and_answers()


    def question_and_answers(self):
        self.round_num += 1
        


        random_phobia = random.randint(0, (len(self.phobia_list)-1))
        correct_phobia = self.phobia_list[random_phobia]
        print("{}is the fear of:".format(correct_phobia))

        correct_fear = self.fear_name_list[random_phobia]
        print(correct_fear)
        
        self.phobia_list.pop(random_phobia)
        self.fear_name_list.pop(random_phobia)
        print(len(self.phobia_list))
        print(len(self.fear_name_list))

        random_fears = random.sample(range(1, len(self.fear_name_list)-1), 3)

        random_fear_1 = random_fears[0]
        random_fear1_name = self.fear_name_list[random_fear_1]

        random_fear_2 = random_fears[1]
        random_fear2_name = self.fear_name_list[random_fear_2]

        random_fear_3 = random_fears[2]
        random_fear3_name = self.fear_name_list[random_fear_3]

        random_num = random.sample(range(1,5),4)

        fear_answers_list = [correct_fear, random_fear1_name, random_fear2_name, random_fear3_name]

        answer1 = fear_answers_list[random_num[0]-1]
        answer2 = fear_answers_list[random_num[1]-1]
        answer3 = fear_answers_list[random_num[2]-1]
        answer4 = fear_answers_list[random_num[3]-1]

        self.answer_button_1.config(text=answer1)
        self.answer_button_2.config(text=answer2)
        self.answer_button_3.config(text=answer3)
        self.answer_button_4.config(text=answer4)

        question_number = "Question {}".format(self.round_num)
        self.question_number_label.config(text=question_number)

        question = "{}is the fear of:".format(correct_phobia)
        self.question_label.config(text=question)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def to_stats(self, quiz_history, quiz_stats):
        QuizStats(self, quiz_history, quiz_stats)
    



# Main Routine
if __name__ == "__main__":
    root= Tk() 
    root.title("Phobia Quiz")
    something = Start(root)
    root.mainloop()