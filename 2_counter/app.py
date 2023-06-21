from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def task_list():
    tasks = ["Выгулять собаку", "Погладить рубашку", "Зайти в супермаркет", 
    "Убрать на кухне", "Дописать статью", "Позвонить тимлиду"]
    return render_template('task_list.html', tasks=tasks)

if __name__ == '__main__':
    app.run()