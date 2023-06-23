import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
img = os.path.join('static', 'img')


@app.route('/')
def index():

    fellow=['Reginald Jean Amedee', "Cassey Shao", "Eyob Dagnachew"]
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), fellow=fellow)




@app.route('/<fellow>')
def fellowPage(fellow):
    fellow=request.args.get('fellow', fellow)
    # if fellow == "Reginald":
    #     hobbyImage1=os.path.join(img, 'elden_ring.png')
    #     hobbyImage2=os.path.join(img, 'reggie_picture.jpg')
    #     experience={"experience": ['Vimeo', 'A Free Bird']}
    #     hobby1="Video Games"
    #     hobby2="Hockey"
    # elif fellow == "Cassey":
    #     hobbyImage1=os.path.join(img, 'elden_ring.png')
    #     hobbyImage2=os.path.join(img, 'reggie_picture.jpg')
    #     experience={"experience": ['College', 'Local']}
    #     hobby1="Coding"
    #     hobby2="Art"
    # elif fellow == "Eyob":
    #     hobbyImage1=os.path.join(img, 'elden_ring.png')
    #     hobbyImage2=os.path.join(img, 'reggie_picture.jpg')
    #     experience={"experience": ['College', 'Local']}
    #     hobby1="Drawing"
    #     hobby2="Dancing"



    return render_template('aboutMePage.html', fellow=fellow)

@app.route('/<fellow>/experience')
def experiencePage(fellow):
    if fellow == "Reginald":
        experience={"experience": ['Vimeo', 'A Free Bird']}
        data="Reginald Jean Amedee"
    elif fellow == "Cassey":
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

    print(fellow)

    return render_template('experiencePage.html', data=data, experience=experience)

@app.route('/<fellow>/hobbies')
def hobbiesPage(fellow):
    if fellow == "Reginald":
        data="Reginald Jean Amedee"
    elif fellow == "Cassey":
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

    return render_template('hobbiesPage.html', data=data)
