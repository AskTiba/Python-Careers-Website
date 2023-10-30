from flask import Flask, render_template

app = Flask(__name__)

jobs = [
    {   
        "id": 1,
        "title": "Data Analyst",
        "location": "Singapore"
    },
    {   
        "id": 2,
        "title": "Project Manager",
        "location": "Ethiopia"
    },
    {   
        "id": 3,
        "title": "Dentist",
        "location": "Sweden"
    },
    {   
        "id": 4,
        "title": "Accountant",
        "location": "Libya"
    },
]

@app.route('/')
def hello():
    return render_template('home.html', work=jobs, company_name="Jolly Job Seekers, Inc.")

if __name__ == '__main__':
    app.run(debug=True)