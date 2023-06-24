import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Landing page data
landing_data = [
    {
        "name": "Reginald Amedee",
        "img": "./static/img/reginald.jpeg",
    },
    {
        "name": "Eyob Dagnachew",
        "img": "./static/img/eyob.jpeg",
    },
    {
        "name": "Cassey Shao",
        "img": "./static/img/cassey.JPG",
    }
]


@app.route('/')
def index():
    intro_message = "Welcome to our page! Click on a fellow to learn more about them!"
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), landing_data=landing_data, intro_message=intro_message)
