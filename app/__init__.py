import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
hobbyImageDir = os.path.join('img')
img = os.path.join('static', 'img')


@app.route('/')
def index():

    fellow=['Reginald Jean Amedee', "Cassey Shao", "Eyob Dagnachew"]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), fellow=fellow)




@app.route('/<fellow>')
def fellowPage(fellow):
    fellow=request.args.get('fellow', fellow)
    return render_template('aboutMePage.html', fellow=fellow)

@app.route('/<fellow>/experience')
def experiencePage(fellow):
    if fellow == "Reginald":
        experience=[{"Vimeo": "Account Manager"}, {"AFreeBird.org": "Web Developer"}]
        data="Reginald Jean Amedee"
    elif fellow == "Cassey":
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

    print(fellow)

    return render_template('experiencePage.html', data=data, experience=experience)

@app.route('/<fellow>/hobbies')
def hobbiesPage(fellow):
    hobbyImage1=os.path.join(hobbyImageDir, 'elden_ring.png')
    hobbyImage2=os.path.join(hobbyImageDir, 'reggie_picture.jpg')

    if fellow == "Reginald":
        data="Reginald Jean Amedee"
        hobbies=[{"Video Games": hobbyImage1}, {"Hockey": hobbyImage2}]
    elif fellow == "Cassey":
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

    return render_template('hobbiesPage.html', data=data, hobbies=hobbies)
