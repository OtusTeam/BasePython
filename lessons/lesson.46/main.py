from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        login1 = request.form['login']
        password = request.form['password']
        if login1 == 'admin' and password == '1234':
            return redirect(url_for('about', name=login1))
        return render_template('login.html')
    return render_template('login.html')


@app.route('/about/<string:name>/')
def about(name):
    return f'Привет, {name}! Эта страница о нашем курсе'


@app.route('/contact/')
def contact():
    context = {
            'title': 'Контакты',
            'tel': '8-800-555-35-35',
            'address': 'Сочи, Краснодарский край',
    }

    return render_template('contacts.html', context=context)


@app.route('/sum/<int:num1>/<int:num2>/')
def sum_numbers(num1, num2):
    result = num1 + num2
    return f'Сумма чисел {num1} и {num2} равна {result}'


@app.route('/len/<string:my_str>/')
def len_str(my_str):  # pylint:disable=missing-function-docstring
    result = len(my_str)
    return f'Длина строки {my_str} равна {result}'


@app.route('/students/')
def students():
    """
    Students view
    :return:
    """
    students1 = [
        {'name': 'Иван', 'course': 1, 'group': 101},
        {'name': 'Петр', 'course': 2, 'group': 201},
        {'name': 'Сидор', 'course': 3, 'group': 301},
    ]
    return render_template('students.html', students=students1)


if __name__ == '__main__':
    app.run(debug=True)
