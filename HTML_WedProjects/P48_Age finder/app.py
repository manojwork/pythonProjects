from flask import Flask,render_template
import requests
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Enter the name in the url</h1>"
@app.route('/<name>')
def display(name):
    gender_url=f"https://api.genderize.io?name={name}"
    age_url=f"https://api.agify.io?name={name}"
    gender_request=requests.get(gender_url)
    gender=gender_request.json()['gender']
    age_request=requests.get(age_url)
    age=age_request.json()['age']
    return render_template('index.html',person_name=name,gender=gender,age=age)

if __name__ == '__main__':
    app.run(debug=True)