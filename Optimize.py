import random
import statistics
import copy


class Player(object):

    def __init__(self, name: str, drinking: float, smoking: float):
        self.name = name
        self.drinking = drinking
        self.smoking = smoking

    def __repr__(self):
        return '{}'.format(self.name)


def total_drinking(team_list: list):
    total = 0
    for player in team_list:
        total += player.drinking
    return 'total drinking = ' + str(total)


def total_smoking(team_list: list):
    total = 0
    for player in team_list:
        total += player.smoking
    return 'total smoking = ' + str(total)


class Team(object):

    def __init__(self, name: str):
        self.team = []
        self.name = name

    def __repr__(self):
        return '{}: {}\n{}\n{}'.format(self.name, self.team, total_drinking(self.team), total_smoking(self.team))

    def append(self, player: Player):
        return self.team.append(player)

    def __iter__(self):
        return self.team.__iter__()


def create_teams(roster: list, team_count: int) -> list:
    temp_roster = copy.copy(roster)
    team_list = []
    for i in range(team_count):
        team_list.append(Team('TEAM {}'.format(i + 1)))

    while len(temp_roster) > 0:
        for team in team_list:
            if len(temp_roster) > 0:
                pick = random.choice(temp_roster)
                team.append(pick)
                temp_roster.remove(pick)

    return team_list


def team_variance(teams: list) -> float:
    if len(teams) == 1:
        return 0

    drinking_totals = []
    smoking_totals = []

    for team in teams:
        drinking_total = 0
        smoking_total = 0

        for player in team:
            drinking_total += player.drinking
            smoking_total += player.smoking

        drinking_totals.append(drinking_total)
        smoking_totals.append(smoking_total)

    return statistics.stdev(drinking_totals) + statistics.stdev(smoking_totals)


def optimize_recursive(roster: list, team_count: int, error_threshold: float) -> list:
    gauntlet = create_teams(roster, team_count)
    if team_variance(gauntlet) > error_threshold:
        return optimize_recursive(roster, team_count, error_threshold)
    else:
        print(gauntlet)
        print('with a SD of: {}'.format(team_variance(gauntlet)))
        return gauntlet


def find_threshold(roster: list, team_count: int, error_threshold=0.0):
    try:
        return optimize_recursive(roster, team_count, error_threshold)
    except RuntimeError:
        return find_threshold(roster, team_count, error_threshold + 0.1)


def optimize_iterative(roster: list, team_count: int) -> list:
    optimal_gauntlet = create_teams(roster, team_count)
    for i in range(100):
        gauntlet = create_teams(roster, team_count)
        if team_variance(gauntlet) < team_variance(optimal_gauntlet):
            optimal_gauntlet = gauntlet
    print(optimal_gauntlet)
    print('with a SD of: {}'.format(team_variance(optimal_gauntlet)))
    return optimal_gauntlet
