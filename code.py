import random
import tkinter as tk
from tkinter import messagebox

class CardMatchChallenge:
    def __init__(self, master):
        self.master = master
        self.master.title("Card Match Challenge")
        self.master.geometry("400x200")

        self.deck = [
            'A ♠', '2 ♠', '3 ♠', '4 ♠', '5 ♠', '6 ♠', '7 ♠', '8 ♠', '9 ♠', '10 ♠', 'A ♥', '2 ♥', '3 ♥', '4 ♥', '5 ♥',
            '6 ♥', '7 ♥', '8 ♥', '9 ♥', '10 ♥', 'A ♦', '2 ♦', '3 ♦', '4 ♦', '5 ♦', '6 ♦', '7 ♦', '8 ♦', '9 ♦', '10 ♦',
            'J ♦', 'J ♣', 'Q ♦', 'Q ♣', 'K ♦', 'K ♣'
        ]

        self.main_papers = self.generate_main_papers()
        self.my_papers = self.generate_my_papers()

        self.passed = 0
        self.rounds_played = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Card Match Challenge", font=("Arial", 16))
        self.label.pack(pady=10)

        self.main_papers_label = tk.Label(self.master, text="Main Papers:")
        self.main_papers_label.pack()

        self.main_papers_frame = tk.Frame(self.master)
        self.main_papers_frame.pack()

        for i, card in enumerate(self.main_papers):
            card_label = tk.Label(self.main_papers_frame, text=card, padx=10)
            card_label.grid(row=0, column=i)

        self.my_papers_label = tk.Label(self.master, text="My Papers:")
        self.my_papers_label.pack()

        self.my_papers_frame = tk.Frame(self.master)
        self.my_papers_frame.pack()

        for i, card in enumerate(self.my_papers):
            card_label = tk.Label(self.my_papers_frame, text=card, padx=10)
            card_label.grid(row=0, column=i)

        self.pass_button = tk.Button(self.master, text="Pass", command=self.pass_turn)
        self.pass_button.pack(pady=10)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_turn)
        self.play_button.pack()

    def generate_main_papers(self):
        main_papers = random.sample(self.deck, 4)
        return main_papers

    def generate_my_papers(self):
        while True:
            my_papers = random.sample(self.deck, 4)
            if self.check_valid_papers(my_papers):
                return my_papers

    def check_valid_papers(self, papers):
        suits = set()
        ranks = set()

        for card in papers:
            suit, rank = card.split()
            suits.add(suit)
            ranks.add(rank)

        if len(suits) == 1 or len(ranks) == 1:
            return False

        return True

    def pass_turn(self):
        self.passed += 1
        self.rounds_played += 1

        if self.passed == 3:
            self.end_game()
        else:
            self.update_game_state()

    def play_turn(self):
        selected_card = random.choice(self.my_papers)
        discarded_card = random.choice(self.main_papers)

        self.my_papers.remove(selected_card)
        self.my_papers.append(discarded_card)
        self.main_papers.remove(discarded_card)
        self.main_papers.append(selected_card)

        self.update_game_state()

        if self.check_game_won():
            self.end_game()

    def update_game_state(self):
        self.my_papers_frame.destroy()
        self.my_papers_frame = tk.Frame(self.master)
        self.my_papers_frame.pack()

        for i, card in enumerate(self.my_papers):
            card_label = tk.Label(self.my_papers_frame, text=card, padx=10)
            card_label.grid(row=0, column=i)

    def check_game_won(self):
        if len(set(self.my_papers)) == 1 or len(set(self.main_papers)) == 1:
            return True
        return False

    def end_game(self):
        messagebox.showinfo("Game Over", "Game has ended!")
        self.master.destroy()

# Create the root window
root = tk.Tk()

# Create an instance of the CardMatchChallenge class with the root window as the master
game = CardMatchChallenge(root)

# Start the Tkinter event loop
root.mainloop()
