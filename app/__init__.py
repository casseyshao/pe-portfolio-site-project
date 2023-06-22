import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():

    experience1={"experience": ['Vimeo', 'A Free Bird']}
    hobbies1={"hobbies": ['Video Games', 'Calisthenics']}
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), experience1=experience1, hobbies1=hobbies1)
