from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
from second import second
from datetime import timedelta
app = Flask(__name__)
app.register_blueprint(second)

app.secret_key = 'h432hi5ohi3h5i5hi3o2hi'
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def home(): 
    return render_template('home.html', codes=session.keys())

if __name__ == "__main__":
    app.run(debug = True)
