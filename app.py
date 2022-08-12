from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thoughts')
def thoughts():
    return render_template('thoughts.html')


if __name__ == '__main__':
    app.run()