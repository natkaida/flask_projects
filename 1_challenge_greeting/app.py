from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        greeting = 'Доброе утро'
    elif now.hour >= 12 and now.hour < 18:
        greeting = 'Добрый день'
    elif now.hour >= 18 and now.hour < 24:
        greeting = 'Добрый вечер'
    else:
        greeting = 'Доброй ночи'
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)