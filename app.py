from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
FILENAME = "students.csv"

# Ensure file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Grade"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']

    if id and name and age and grade:
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, name, age, grade])
    return redirect('/')

@app.route('/view')
def view():
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        records = list(reader)
    return render_template('view.html', records=records)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

