from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    students1 = [
        {'name': 'Иван', 'course': 1, 'group': 101},
        {'name': 'Петр', 'course': 2, 'group': 201},
        {'name': 'Сидор', 'course': 3, 'group': 301},
        {'name': 'Иван', 'course': 1, 'group': 101},
        {'name': 'Петр', 'course': 2, 'group': 201},
        {'name': 'Сидор', 'course': 3, 'group': 301},
    ]
    return render_template('index.html', students=students1)



if __name__ == '__main__':
    app.run(debug=True)
