from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Чтение данных из CSV файла
def read_csv() -> list:
    users = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users

# Запись данных в CSV файл
def write_csv(users):
    with open('data.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'age', 'city']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow(user)

@app.route('/')
def index():
    users = read_csv()
    return render_template('index.html', users=users)

@app.route('/user/<int:user_id>')
def user(user_id):
    users = read_csv()
    user = next((u for u in users if int(u['id']) == user_id), None)
    if user:
        return render_template('user.html', user=user)
    else:
        return "User not found", 404

@app.route('/delete/<int:user_id>')
def delete(user_id):
    users = read_csv()
    users = [u for u in users if int(u['id']) != user_id]
    write_csv(users)
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_name = request.form['name']
        new_age = request.form['age']
        new_city = request.form['city']
        users = read_csv()
        new_id = max(int(user['id']) for user in users) + 1
        users.append({'id': new_id, 'name': new_name, 'age': new_age, 'city': new_city})
        write_csv(users)
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/js_1')
def js_example_1():
    return render_template('js_example_1.html')

if __name__ == '__main__':
    app.run(debug=True)
