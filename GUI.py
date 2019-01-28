from tkinter import *
from Optimize import *
from tkinter import messagebox

player_entry_list = []


class PlayerEntry(object):

    def __init__(self, frame, index: int):
        self.index = index
        self.name = Entry(frame, bg='black', fg='cyan', bd=0,
                          insertbackground='cyan', justify=CENTER,
                          takefocus=1, width=12, font=14)
        self.OTR_drinking = Entry(frame, bg='black', fg='green', bd=0,
                                  insertbackground='green', justify=CENTER,
                                  takefocus=1, width=12, font=14)
        self.DVC_drinking = Entry(frame, bg='black', fg='red', bd=0,
                                  insertbackground='red', justify=CENTER,
                                  takefocus=1, width=12, font=14)
        self.OTR_smoking = Entry(frame, bg='black', fg='green', bd=0,
                                 insertbackground='green', justify=CENTER,
                                 takefocus=1, width=12, font=14)
        self.DVC_smoking = Entry(frame, bg='black', fg='red', bd=0,
                                 insertbackground='red', justify=CENTER,
                                 takefocus=1, width=12, font=14)
        self.delete = Button(frame, text='Remove Player', width=9, takefocus=0
                             command=lambda: delete_player(self, player_entry_list))

    def __repr__(self):
        return 'Player {}'.format(str(self.index))

    def set(self):
        self.name.grid(row=self.index, column=0)
        self.OTR_drinking.grid(row=self.index, column=1)
        self.DVC_drinking.grid(row=self.index, column=2)
        self.OTR_smoking.grid(row=self.index, column=3)
        self.DVC_smoking.grid(row=self.index, column=4)
        self.delete.grid(row=self.index, column=5)

    def delete(self):
        self.name.grid_forget()
        self.OTR_drinking.grid_forget()
        self.DVC_drinking.grid_forget()
        self.OTR_smoking.grid_forget()
        self.DVC_smoking.grid_forget()
        self.delete.grid_forget()


def test_player(player: PlayerEntry):
    score_list = [player.OTR_drinking, player.DVC_drinking, player.OTR_smoking, player.DVC_smoking]
    for entry in score_list:
        try:
            float(entry.get())
        except ValueError:
            return False
        if float(entry.get()) < 0 or float(entry.get()) > 5.5:
            return False
    return True


def test_teamcount(entry, player_count):
    try:
        int(entry.get())
    except ValueError:
        return False
    if int(entry.get()) < 1 or int(entry.get()) > player_count:
        return False
    return True


def new_player(frame, index: int, button):
    bad_input = False
    for player in player_entry_list:
        if not test_player(player):
            bad_input = True

    if bad_input:
        messagebox.showerror('Error', 'WTF is that?? '
                                      'All scores have to be '
                                      'between 0 and 5!')

    player = PlayerEntry(frame, index)
    player.set()
    player_entry_list.append(player)
    button.grid_forget()
    add_player = Button(frame, text='Add Player', width=9, takefocus=0,
                        command=lambda: new_player(frame, index + 1, add_player))
    add_player.grid()

    return


def delete_player(player, player_entry_list):
    player.name.grid_forget()
    player.OTR_drinking.grid_forget()
    player.DVC_drinking.grid_forget()
    player.OTR_smoking.grid_forget()
    player.DVC_smoking.grid_forget()
    player.delete.grid_forget()
    player_entry_list.remove(player)
    return


def display_results(teams):
    results = ''
    for team in teams:
        results += str(team) + '\n\n'
    results += 'Variance Score: ' + str(round(team_variance(teams), 2))
    return results


def calculate_teams(team_count: Entry):
    for player in player_entry_list:
        if not test_player(player):
            messagebox.showerror('Error', 'Ya dun fucked up. Go back and make '
                                          'sure all scores are between 0 and 5.')
            return

    if not test_teamcount(team_count, len(player_entry_list)):
        messagebox.showerror('Error', "You fool! Number of teams has to be "
                                      "a positive, whole number and it can't "
                                      "be more than number of players.")
        return

    roster = []
    for player in player_entry_list:
        name = player.name.get()
        drinking_score = (float(player.OTR_drinking.get()) + float(player.DVC_drinking.get())) / 2
        smoking_score = (float(player.OTR_smoking.get()) + float(player.DVC_smoking.get())) / 2
        roster.append(Player(name, drinking_score, smoking_score))
    groups = find_threshold(roster, int(team_count.get()))
    messagebox.showinfo('Results', display_results(groups))
