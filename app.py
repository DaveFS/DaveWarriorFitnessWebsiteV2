from flask import Flask, render_template, jsonify

app = Flask(__name__)

WORKOUTS = [
    {
        'id' : 1,
        'title' : 'Easy Starter',
        'location' : 'online',
        'duration' : '20min',
    },
    {
        'id' : 2,
        'title' : 'Train to Failure',
        'location' : 'online',
        'duration' : '45min',
        'cost' : '£22 - first 2 sessions, £35 thereafter'
    },
    {
        'id' : 3,
        'title' : 'The Punisher',
        'location' : 'Face to Face',
        'duration' : '60min',
        'cost' : '£30'
    },
    {
        'id' : 4,
        'title' : 'Progress is Progress',
        'location' : 'online',
        'duration' : '30min',
        'cost' : '£10'
    },
]

@app.route("/")
def dave_site():
    return render_template('home.html',
    workouts = WORKOUTS)

@app.route("/workouts")
def list_workouts():
    return jsonify(WORKOUTS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)