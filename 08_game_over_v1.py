from tkinter import *
import random
from functools import partial # To prevent unwanted windows
from datetime import datetime # To get date and time of export


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10, bg="#F8F9FA") 
        self.start_frame.grid()

        # Mstery Heading (row 0)
        self.start_label = Label(self.start_frame, text="Phobia Quiz",
                                       font="Arial 19 bold", bg="#F8F9FA")
        self.start_label.grid(row=0)

        # initial instructions (row 1)
        self.quiz_intructions = Label(self.start_frame, font="Arial 10 italic", bg="#F8F9FA",
                                         text="This is a quiz where you get given a question asking what a certain phobia is the fear of and you get given 4 multiple choice answers to choose from."
                                              "There are 108 Phobias in this quiz shown in a random order but you can check your stats and quit at any point",
                                         wrap=275, justify=LEFT, padx=10, pady=10)
        self.quiz_intructions.grid(row=1)

        # Play frame (row 2)
        self.play_frame = Frame(self.start_frame, bg="#F8F9FA")
        self.play_frame.grid(row=2)

        # Play button
        self.play_button = Button(self.play_frame, text="Play",
                                       command=lambda: self.to_quiz(),
                                       font="Arial 15 bold", bg="#CED4DA")
        self.play_button.grid(row=0, column=0, pady=10)


    def to_quiz(self):

        Quiz(self)

        # hide start up window
        root.withdraw()



class Quiz:
    def __init__(self, partner):

        self.number_correct = 0
        self.number_wrong = 0
        
        # List for holding statistics
        self.round_stats_list = []

        self.phobia_list = ['Achluophobia ', 'Acousticophobia ', 'Acrophobia ']
        # list of all phobias
        # self.phobia_list = ['Achluophobia ', 'Acousticophobia ', 'Acrophobia ', 'Agoraphobia ', 'Agyrophobia ', 'Aichmophobia ', 'Ailurophobia ', 'Algophobia ', 'Ancraophobia ', 
        # 'Arachnophobia ', 'Astraphobia ', 'Autophobia ', 'Bacteriophobia ', 'Basophobia ', 'Batrachophobia ', 'Belonephobia ', 'Bibliophobia ', 'Cacophobia ', 'Carcinophobia ', 
        # 'Catoptrophobia ', 'Chemophobia ', 'Cherophobia ', 'Chiroptophobia ', 'Chromophobia ', 'Chronomentrophobia ', 'Chronophobia ', 'Cibophobia ', 'Claustrophobia ', 'Coimetrophobia ', 
        # 'Coulrophobia ', 'Cyberphobia ', 'Cynophobia ', 'Demonophobia ', 'Dendrophobia ', 'Dentophobia ', 'Domatophobia ', 'Emetophobia ', 'Enochlophobia ', 'Entomophobia ', 'Ephebiphobia ', 
        # 'Equinophobia ', 'Ergophobia ', 'Frigophobia ', 'Gamophobia ', 'Gephyrophobia ', 'Gerascophobia ', 'Germophobia ', 'Globophobia ', 'Glossophobia ', 'Halitophobia ', 'Heliophobia ', 
        # 'Helminthophobia ', 'Hemophobia ', 'Herpetophobia ', 'Hexakosioihexekontahexaphobia ', 'Hodophobia ', 'Hydrophobia ', 'Hypochondria ', 'Ichthyophobia ', 'Koumpounophobia ', 
        # 'Lepidopterophobia ', 'Lilapsophobia ', 'Mageirocophobia ', 'Melanophobia ', 'Melissophobia ', 'Monophobia ', 'Musophobia ', 'Myrmecophobia ', 'Necrophobia ', 'Neophobia ', 'Noctiphobia ', 
        # 'Nosocomephobia ', 'Numerophobia ', 'Nyctophobia ', 'Obesophobia ', 'Ommetaphobia ', 'Oneirophobia ', 'Ophidiophobia ', 'Ornithophobia ', 'Osmophobia ', 'Ostraconophobia ', 'Panphobia ', 
        # 'pediaphobia ', 'Pharmacophobia ', 'Phasmophobia ', 'Phobophobia ', 'Phonophobia ', 'Pogonophobia ', 'Porphyrophobia ', 'Pteromerhanophobia ', 'Pyrophobia ', 'Radiophobia ', 
        # 'Siderodromophobia ', 'Sociophobia ', 'Somniphobia ', 'Taphophobia ', 'Technophobia ', 'Tetraphobia ', 'Thalassophobia ', 'Thanatophobia ', 'Thermophobia ', 
        # 'Toxiphobia ', 'Traumatophobia ', 'Trichophobia ', 'Triskaidekaphobia ','Vehophobia ', 'Xanthophobia ', 'Xenophobia '
        #]

        self.fear_name_list = ['darkness', 'noise', 'heights']
        # list of all the names for the phobias
        # self.fear_name_list = ['darkness', 'noise', 'heights', 'open spaces', 'crossing streets', 'sharp objects', 'cats', 'pain', 'wind', 'spiders', 'thunder and lightning',
        # 'isolation', 'bacteria', 'falling', 'frogs', 'needles', 'books', 'ugliness', 'cancer', 'mirrors', 'chemicals', 'happiness', 'bats', 'colours', 'clocks', 'time passing', 'food', 
        # 'closed spaces', 'cemetries', 'clowns', 'computers', 'dogs', 'demons', 'trees', 'dentists', 'houses', 'vomiting', 'crowds', 'insects', 'youth', 'horses', 'work', 'cold', 'marriage', 
        # 'bridges', 'aging', 'germs', 'balloons', 'public speaking', 'bad breath', 'sunlight', 'worms', 'blood', 'reptiles', '666', 'travel', 'water', 'illness', 'fish', 'buttons', 
        # 'butterflies', 'tornadoes or hurricanes', 'cooking', 'black', 'bees', 'being alone', 'mice', 'ants', 'death', 'new things', 'night', 'hospitals', 'numbers', 'darkness', 
        # 'weight gain', 'eyes', 'dreams', 'snakes', 'birds', 'smells', 'shellfish', 'everything', 'babies and children', 'medicine', 'ghosts', 'fear', 'loud sounds', 'beards', 'purple', 
        # 'flying', 'fire', 'radioactivity', 'trains', 'people', 'sleep', 'graves', 'technology', '4', 'sea', 'dying', 'heat', 'poisons', 'injury', 'hair loss', '13', 
        # 'driving', 'yellow', 'foreigners'
        # ]

        # duplicate fears list for random answers
        self.all_fears = ['darkness', 'noise', 'heights', 'open spaces', 'crossing streets', 'sharp objects', 'cats', 'pain', 'wind', 'spiders', 'thunder and lightning',
        'isolation', 'bacteria', 'falling', 'frogs', 'needles', 'books', 'ugliness', 'cancer', 'mirrors', 'chemicals', 'happiness', 'bats', 'colours', 'clocks', 'time passing', 'food', 
        'closed spaces', 'cemetries', 'clowns', 'computers', 'dogs', 'demons', 'trees', 'dentists', 'houses', 'vomiting', 'crowds', 'insects', 'youth', 'horses', 'work', 'cold', 'marriage', 
        'bridges', 'aging', 'germs', 'balloons', 'public speaking', 'bad breath', 'sunlight', 'worms', 'blood', 'reptiles', '666', 'travel', 'water', 'illness', 'fish', 'buttons', 
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
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=lambda: self.right_wrong(1))
        self.answer_button_1.grid(row=0, column=1, padx=2, pady=2)


        self.answer_button_2 = Button(self.box_frame, text=answer2, bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=lambda: self.right_wrong(2))
        self.answer_button_2.grid(row=0, column=2, padx=2, pady=2)


        self.answer_button_3 = Button(self.box_frame, text="Answer Buttons", bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=lambda: self.right_wrong(3))
        self.answer_button_3.grid(row=1, column=1, padx=2, pady=2)

        self.answer_button_4 = Button(self.box_frame, text="self.answer_button_4", bg="#CED4DA",
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=lambda: self.right_wrong(4))
        self.answer_button_4.grid(row=1, column=2, padx=2, pady=2)


        # Next Question Button (row 5)
        self.next_button_frame = Frame(self.quiz_frame, bg="#F8F9FA")
        self.next_button_frame.grid(row=5, pady=10)

        self.next_button = Button(self.next_button_frame, text="Next Question", font=("Arial 14 bold"),
                                   bg="#CED4DA", 
                                   command=self.question_and_answers)
        self.next_button.grid(row=0, column=2, padx=2)

        # disable next button until user answers question
        self.next_button.config(state=DISABLED)
    
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

        self.stats_button.config(state=DISABLED)

        self.question_and_answers()
    
    def play_again(self):

        # hide start up window
        self.quiz_box.destroy()
        Quiz(self)


    # generates questions and answers
    def question_and_answers(self):

        # after round 1 enable stats button
        if self.round_stats_list != []:
            self.stats_button.config(state=NORMAL)

        # resets buttons for next question
        self.next_button.config(state=DISABLED)

        self.answer_button_1.config(state=NORMAL)
        self.answer_button_2.config(state=NORMAL)
        self.answer_button_3.config(state=NORMAL)
        self.answer_button_4.config(state=NORMAL)

        self.answer_button_1.config(bg="#CED4DA")
        self.answer_button_2.config(bg="#CED4DA")
        self.answer_button_3.config(bg="#CED4DA")
        self.answer_button_4.config(bg="#CED4DA")

        if len(self.phobia_list) == 0:
            print("Game Over")

            self.answer_button_1.config(state=DISABLED, text="")
            self.answer_button_2.config(state=DISABLED, text="")
            self.answer_button_3.config(state=DISABLED, text="")
            self.answer_button_4.config(state=DISABLED, text="")

            self.question_label.config(font=("arial 10"), text="You have answered all the questions. You can view/save your stats, play again, or Quit")
            self.question_number_label.config(text="Game Over", font="Arial 15 bold")

            self.next_button.config(state=NORMAL, text="Play Again", command=lambda: self.play_again())

            self.help_button.config(state=DISABLED)

        else:
            # add to round counter
            self.round_num += 1

            # generates correct phobia
            random_phobia = random.randint(0, (len(self.phobia_list)-1))
            correct_phobia = self.phobia_list[random_phobia]

            self.correct_fear = self.fear_name_list[random_phobia]
            print("correct fear: {}".format(self.correct_fear))
            
            # removes used phobia from list (until end of Quiz)
            self.phobia_list.pop(random_phobia)
            self.fear_name_list.pop(random_phobia)

            # generates 3 random fears
            self.random_fears = random.sample(range(1, len(self.all_fears)-1), 3)
            # get the fear names for the phobias
            random_fear_1 = self.random_fears[0]
            random_fear_2 = self.random_fears[1]
            random_fear_3 = self.random_fears[2]
            self.random_fear_names = [self.all_fears[random_fear_1], self.all_fears[random_fear_2], self.all_fears[random_fear_3]]


            # loop random fear generation untill its not the same as the correct answer
            while self.correct_fear in self.random_fear_names:
                if self.correct_fear in self.random_fear_names:
                    self.random_fears = random.sample(range(1, len(self.all_fears)-1), 3)
                    random_fear_1 = self.random_fears[0]
                    random_fear_2 = self.random_fears[1]
                    random_fear_3 = self.random_fears[2]
                    self.random_fear_names = [self.all_fears[random_fear_1], self.all_fears[random_fear_2], self.all_fears[random_fear_3]]
                    continue
                else:
                    break

            # get fear names from all fear list
            random_fear_1 = self.random_fears[0]
            random_fear1_name = self.all_fears[random_fear_1]

            random_fear_2 = self.random_fears[1]
            random_fear2_name = self.all_fears[random_fear_2]

            random_fear_3 = self.random_fears[2]
            random_fear3_name = self.all_fears[random_fear_3]


            # arranges random and correct fears randomly
            random_num = random.sample(range(1,5),4)
            fear_answers_list = [self.correct_fear, random_fear1_name, random_fear2_name, random_fear3_name]

            answer1 = fear_answers_list[random_num[0]-1]
            answer2 = fear_answers_list[random_num[1]-1]
            answer3 = fear_answers_list[random_num[2]-1]
            answer4 = fear_answers_list[random_num[3]-1]

            # assigns randomly ordered fears to the buttons
            self.answer_button_1.config(text=answer1)
            self.answer_button_2.config(text=answer2)
            self.answer_button_3.config(text=answer3)
            self.answer_button_4.config(text=answer4)

            # question / round number
            question_number = "Question {}".format(self.round_num)
            self.question_number_label.config(text=question_number)

            # question
            self.question = "{}is the fear of".format(correct_phobia)
            self.question_label.config(text=self.question)

    # tells user if answer is right or wrong
    def right_wrong(self, button):

        # disables answer buttons after user chooses one
        self.answer_button_1.config(state=DISABLED)
        self.answer_button_2.config(state=DISABLED)
        self.answer_button_3.config(state=DISABLED)
        self.answer_button_4.config(state=DISABLED)

        correct = False

        # checks if answers are correct or incorrect and colours buttons accordingly (red if wrong and green if right)
        if button == 1:
            chosen_answer = self.answer_button_1['text']
            if self.answer_button_1['text'] == self.correct_fear:
                self.number_correct += 1

                self.answer_button_1.config(bg="#83cf5f")
                correct = True
            else:
                self.answer_button_1.config(bg="#ff6b6b")
                correct = False
        elif button == 2:
            chosen_answer = self.answer_button_2['text']
            if self.answer_button_2['text'] == self.correct_fear:
                self.number_correct += 1
                
                self.answer_button_2.config(bg="#83cf5f")
                correct = True
            else:
                self.answer_button_2.config(bg="#ff6b6b")
                correct = False
        elif button == 3:
            chosen_answer = self.answer_button_3['text']
            if self.answer_button_3['text'] == self.correct_fear:
                self.number_correct += 1

                self.answer_button_3.config(bg="#83cf5f")
                correct = True
            else:
                self.answer_button_3.config(bg="#ff6b6b")
                correct = False
        else:
            chosen_answer = self.answer_button_4['text']
            if self.answer_button_4['text'] == self.correct_fear:
                self.number_correct += 1
                
                self.answer_button_4.config(bg="#83cf5f")   
                correct = True
            else:
                self.answer_button_4.config(bg="#ff6b6b")
                correct = False

        # if user chooses wrong answer highlight correct answer in orange
        if correct == False:
            self.number_wrong += 1 
            if self.answer_button_1['text'] == self.correct_fear:
                self.answer_button_1.config(bg="#ffb73a")
            elif self.answer_button_2['text'] == self.correct_fear:
                self.answer_button_2.config(bg="#ffb73a")
            elif self.answer_button_3['text'] == self.correct_fear:
                self.answer_button_3.config(bg="#ffb73a")
            elif self.answer_button_4['text'] == self.correct_fear:
                self.answer_button_4.config(bg="#ffb73a")

        # activate next button
        self.next_button.config(state=NORMAL)


        # add results to quiz stats list
        self.quiz_stats_list = [self.round_num, self.number_correct, self.number_wrong]

        # add round results to statistics list
        round_summary = "Round {} | Question: {} | Chosen answer: {} | Correct answer: {} ".format(self.round_num, self.question, chosen_answer, self.correct_fear)
        self.round_stats_list.append(round_summary)
        print(round_summary)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="choose an answer for the question then press next question for a new question.")

    def to_stats(self, quiz_history, quiz_stats):
        QuizStats(self, quiz_history, quiz_stats)





class QuizStats:
    def __init__(self, partner, quiz_history, quiz_stats):

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box,)
        self.stats_frame.grid()

        # Set up stats heading row 0
        self.stats_heading_label = Label(self.stats_frame, text="Quiz Statistics", padx=20,
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # detatils frame (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Rounds Played (row 0)
        self.rounds_played_label = Label(self.details_frame, text="Rounds Played",
                                        font=heading, anchor="e")
        self.rounds_played_label.grid(row=0, column=0, padx=0)

        rounds = quiz_stats[0]

        self.rounds_number_label = Label(self.details_frame, text=rounds,
                                        font=content, anchor="w")
        self.rounds_number_label.grid(row=0, column=1, padx=0)


        # correct (row 1)
        self.correct_label = Label(self.details_frame,
                                         text="Correct:", font=heading,
                                         anchor="e")
        self.correct_label.grid(row=1, column=0, padx=0)

        correct = quiz_stats[1]

        self.correct_number_label = Label(self.details_frame, font=content,
                                               text=correct,
                                               anchor="w")
        self.correct_number_label.grid(row=1, column=1, padx=0)

        # incorrect (row 2)
        self.incorrect_label = Label(self.details_frame,
                                         text="Incorrect:", font=heading,
                                         anchor="e")
        self.incorrect_label.grid(row=2, column=0, padx=0)

        incorrect = quiz_stats[2]

        self.incorrect_number_label = Label(self.details_frame, font=content,
                                               text=incorrect,
                                               anchor="w")
        self.incorrect_number_label.grid(row=2, column=1, padx=0) 

        percentage_correct = (correct / (rounds))*100 

        if percentage_correct == 100:
            percentage_fg = "green"
        elif percentage_correct == 0:
            percentage_fg = "#af4141"
        else:
            percentage_fg = "#000000"

        # percentage correct (row 3)
        self.percentage_label = Label(self.details_frame, text="Percentage Correct",
                                     font=heading, anchor="e", fg=percentage_fg)
        self.percentage_label.grid(row=3, column=0, padx=0)

        self.percentage_value_label = Label(self.details_frame, text=" {:.0f}%".format(percentage_correct),
                                     font=content, anchor="w", fg=percentage_fg)
        self.percentage_value_label.grid(row=3, column=1, padx=0)

        # Export / Dismiss button (row 4)
        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=4, pady=10)


        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export", bg="#CED4DA",
                                    font="arial 12 bold",
                                    command=lambda: self.export(quiz_history, quiz_stats))
        self.export_button.grid(row=0, column=0, padx=2)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", bg="#CED4DA",
                                    font="arial 12 bold",
                                    command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1, padx=2)

        self.quit_frame = Frame(self.stats_frame)
        self.quit_frame.grid(row=5)

    def close_stats(self, partner):
        # Put stats button back to normal
        try:
            partner.stats_button.config(state=NORMAL)
        except:
            print()
        finally:
            self.stats_box.destroy()


    def export(self, quiz_history, quiz_stats):
        Export(self, quiz_history, quiz_stats)

            
class Help:
    def __init__(self, partner):

        background = "#F8F9FA"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help",
                                    font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                                justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", fg="black",
                                    width=10, bg="#CED4DA", font="arial 10 bold",
                                    command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal..
        try:
            partner.help_button.config(state=NORMAL)
        except:
            print()
        finally:
            self.help_box.destroy()

        
class Export:
    def __init__(self, partner, quiz_history, quiz_stats):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and releases export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                    font="arial 19 bold")
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename and press save to make a text file with your stats and full round details of the quiz"
                                    ,justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter already exists it will be replaced"
                                    ,justify=LEFT, bg="#ffafaf", fg="maroon", font="Arail 10 italic",
                                    wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save", font="Arial 15 bold",
                                    bg="#CED4DA", fg="black",
                                    command=partial(lambda: self.save_history(partner, quiz_history, quiz_stats)))
        self.save_button.grid(row=0, column=0, padx=2)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="Arial 15 bold",
                                    bg="#CED4DA", fg="black", 
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1, padx=2)

    def save_history(self, partner, quiz_history, quiz_stats):

        # Regular expression to chack filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        
        else:
            # percentage correct
            percentage_correct = (quiz_stats[1] / (quiz_stats[0]))*100 

            # If there are no errors, generate text file and close dialogue add .txt suffix
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # gets todays date
            today = datetime.today()
            date_time = today.strftime("%d/%m/%Y %H:%M")

            # title and date for txt file
            f.write("Quiz Statistics {}\n\n".format(date_time))

            # Starting Balance
            f.write("Round {}\n".format(quiz_stats[0]))

            # Current Balance
            f.write("Correct: {}\n".format(quiz_stats[1]))

            # amount won / lost
            f.write("Incorrect: {} \n".format(quiz_stats[2]))

            f.write("Percentage Correct: {:.0f}% \n".format(percentage_correct))

            # Heading for Rounds
            f.write("\nFull Round Details\n\n")

            # add new line at end of each item
            for item in quiz_history:
                f.write(item + "\n")

            # close file
            f.close()
            
            # close export window after writing to file
            partner.export_button.config(state=NORMAL)
            self.export_box.destroy()

        
    # lets export window close after stats window is already closed
    def close_export(self, partner):
        # Put export button back to normal..
        try:
            partner.export_button.config(state=NORMAL)
        except:
            print()
        finally:
            self.export_box.destroy()




# Main Routine
if __name__ == "__main__":
    root= Tk() 
    root.title("Phobia Quiz")
    something = Start(root)
    root.mainloop()