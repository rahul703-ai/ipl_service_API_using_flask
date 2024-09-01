from flask import Flask, jsonify, request

import ipl
import jugad

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/api/teams')
def teams():
    all_teams = ipl.teamsAPI()
    return jsonify(all_teams)
    # return "Teams wala api"


@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamvteamAPI(team1, team2)
    return jsonify(response)

    # return team1 + " " + team2


@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = jugad.teamAPI(team_name)
    return response


@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = jugad.batsmanAPI(batsman_name)
    return response


@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = jugad.bowlerAPI(bowler_name)
    return response


app.run(debug=True)
