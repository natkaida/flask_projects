from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<user>')
def user_page(user):
    user_level = user
    return render_template('welcome.html', user_level=user_level)

if __name__ == '__main__':
    app.run()