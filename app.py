from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
FILENAME = "students.csv"

# Create the CSV file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Age", "Grade"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    id = request.form.get('id')
    name = request.form.get('name')
    age = request.form.get('age')
    grade = request.form.get('grade')

    if id and name and age and grade:
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, name, age, grade])
        print(f"Added: {id}, {name}, {age}, {grade}")
    else:
        print("Missing data. Not saved.")

    return redirect('/')

@app.route('/view')
def view():
    with open(FILENAME, "r") as f:
        reader = csv.reader(f)
        records = list(reader)
    return render_template('view.html', records=records)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
