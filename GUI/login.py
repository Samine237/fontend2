import tkinter as tk
from tkinter import messagebox
from model.Player_model import Player

class PlayerForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Créer un nouveau joueur")
        self.geometry("350x330")

        self.player_name_label = tk.Label(self, text="Nom du joueur:")
        self.player_name_entry = tk.Entry(self)

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self)


        self.save_button = tk.Button(self, text="Enregistrer", command=self.save_player)

        self.player_name_label.pack()
        self.player_name_entry.pack()
        self.email_label.pack()
        self.email_entry.pack()
        self.save_button.pack()

    def save_player(self):
        player_name = self.player_name_entry.get()
        email = self.email_entry.get()
        rank = 0
        nb_games_played = 0
        nb_games_won = 0
        nb_games_loosed = 0

        player = Player(player_name=player_name, email=email, rank=rank,
                        nb_game_played=nb_games_played, nb_game_loosed=nb_games_loosed,
                        nb_game_won=nb_games_won)

        try:
            player.create()
            messagebox.showinfo("Succès", "Le joueur a été enregistré avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'enregistrement du joueur: {str(e)}")

if __name__ == "__main__":
    app = PlayerForm()
    app.mainloop()
