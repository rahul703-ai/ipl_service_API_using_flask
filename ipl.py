import pandas as pd
import numpy as np

matches = pd.read_csv(r"C:\Users\RAHUL\PycharmProjects\ipl-api-service\ipl-matches.csv")

print(matches.head())


def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict = {
        'teams': teams
    }

    return team_dict


def teamvteamAPI(team1, team2):
    temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (
                matches['Team2'] == team1)]
    total_matches = temp_df.shape[0]

    matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

    draws = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        'total_matches': str(total_matches),
        team1 + ' won': str(matches_won_team1),
        team2 + ' won': str(matches_won_team2),
        'draws': str(draws)
    }

    return response
