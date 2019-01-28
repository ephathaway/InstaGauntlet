from GUI import *


def main():
    main_window = Tk()
    main_window.title('InstaGauntlet')
    main_window.geometry('726x815')
    main_window.configure(background='Gray20')

    upper_frame = Frame(main_window, bg='Gray20',  width=726)
    upper_frame.pack(anchor=W, padx=10)

    separator = Frame(main_window, bg='Gray20',  width=726, height=10)
    separator.pack(anchor=W)

    instructions_frame = Frame(main_window, bg='Gray20', width=726)
    instructions_frame.pack(anchor=W, padx=10)

    separator = Frame(main_window, bg='Gray20', width=726, height=10)
    separator.pack(anchor=W)

    labels_frame = Frame(main_window, bg='Gray20', width=726, height=60)
    labels_frame.pack(anchor=W)

    edge_frame = Frame(labels_frame, width=10.2, height=40, bg='Gray20')
    edge_frame.grid(row=0, column=0)
    name_frame = Frame(labels_frame, width=116, height=40, bg='black', bd=10)
    name_frame.grid(row=0, column=1)
    name_frame.pack_propagate(False)
    otrd_frame = Frame(labels_frame, width=116, height=40, bg='black')
    otrd_frame.grid(row=0, column=2)
    otrd_frame.pack_propagate(False)
    dvcd_frame = Frame(labels_frame, width=116, height=40, bg='black')
    dvcd_frame.grid(row=0, column=3)
    dvcd_frame.pack_propagate(False)
    otrs_frame = Frame(labels_frame, width=116, height=40, bg='black')
    otrs_frame.grid(row=0, column=4)
    otrs_frame.pack_propagate(False)
    dvcs_frame = Frame(labels_frame, width=116, height=40, bg='black')
    dvcs_frame.grid(row=0, column=5)
    dvcs_frame.pack_propagate(False)
    edge = Frame(labels_frame, width=146, height=40, bg='Gray20')
    edge.grid(row=0, column=6)

    outer_frame = Frame(main_window, bg='Gray20', height=500)
    outer_frame.pack(fill=X)
    outer_frame.pack_propagate(False)

    separator = Frame(main_window, bg='Gray20', width=726, height=10)
    separator.pack(anchor=W)

    team_frame = Frame(main_window, bg='Gray20')
    team_frame.pack(anchor=W, padx=10)

    canvas = Canvas(outer_frame, bg='Gray20')
    root = Frame(canvas)

    scrollbar = Scrollbar(outer_frame, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side='right', fill='y')
    canvas.pack(fill=X)

    canvas.create_window((0, 0), window=root, anchor='nw', height=2000, width=726)
    root.configure(bg='Gray20', padx=10)
    canvas.configure(scrollregion=canvas.bbox('all'), height=2000, width=726)

    welcome = Label(upper_frame, text='WELCOME TO MU FUGGIN GAUNTLET',
                    bg='Gray20', fg='cyan', font=('arial', 20))
    welcome.pack()

    instructions = Label(instructions_frame, text="So you're the lucky soul who's "
                                                  "been put in charge of making "
                                                  "the teams for gauntlet "
                                                  "this year, but you have absolutely "
                                                  "no idea where to begin! "
                                                  "Well fortunately for you, "
                                                  "you've come to the right place. "
                                                  "I will not only take away "
                                                  "the tedious task of "
                                                  "creating teams, I'll make the "
                                                  "teams more evenly matched than "
                                                  "you ever could; even if you "
                                                  "stayed up all night (no offense).\n\n"
                                                  "So let's get to it. Hit the Add "
                                                  "Player button to start entering "
                                                  "player info. Each player needs a "
                                                  "name, 2 drinking scores, and 2 "
                                                  "smoking scores. When you have "
                                                  "entered info for all the players, "
                                                  "enter the number of teams you "
                                                  "want and hit Make Teams. Then "
                                                  "just sit back and watch me work. "
                                                  "Happy Gauntletting!\n",
                         justify=LEFT, wraplength=706, bg='Gray20', fg='cyan')
    instructions.pack()

    name = Label(name_frame, text='Name', bg='black', fg='cyan', font=('arial', 14, 'bold'))
    name.pack()
    otrd = Label(otrd_frame, text='OTR Drinking \n Score', bg='black', fg='green', font=('arial', 14, 'bold'))
    otrd.pack()
    dvcd = Label(dvcd_frame, text='DVC Drinking \n Score', bg='black', fg='red', font=('arial', 14, 'bold'))
    dvcd.pack()
    otrs = Label(otrs_frame, text='OTR Smoking \n Score', bg='black', fg='green', font=('arial', 14, 'bold'))
    otrs.pack()
    dvcs = Label(dvcs_frame, text='DVC Smoking \n Score', bg='black', fg='red', font=('arial', 14, 'bold'))
    dvcs.pack()

    add_player = Button(root, text='Add Player', width=9, takefocus=0,
                        command=lambda: new_player(root, 0, add_player))
    add_player.grid()

    team_label = Label(team_frame, text='Number of Teams:  ', bg='Gray20', fg='cyan', font=('arial', 14, 'bold'))
    team_label.grid(column=0, row=0)
    team_count = Entry(team_frame, bg='black', fg='cyan',
                       bd=0, insertbackground='cyan', justify=CENTER,
                       takefocus=1, width=12, font=14)
    team_count.grid(column=1, row=0)
    make_teams = Button(team_frame, text='Make Teams', width=9, takefocus=0,
                        command=lambda: calculate_teams(team_count))
    make_teams.grid(column=1, row=1)

    main_window.mainloop()


main()
