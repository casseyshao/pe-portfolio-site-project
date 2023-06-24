import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
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
        experience=[{"Company" : "Vimeo", "Role": "Account Manager", "JobDescription": ['Recommended brand products to customers, highlighted benefits and redirected objections to secure more than $1,000,000 in upsell.',
'Worked in an agile environment with Technical Program Managers to ensure that Vimeo’s services are correctly implemented at deadlines that are set.']},{"Company" : "AFreeBird.org", "Role": "Web Enigneer", "JobDescription": ['Making website more responsive on various screen sizes.',
'Lead Developer on a proprietary solution that will save over $5000 a year', 'Built out database models and backend using Django and Python according to system design requirements.']}, {"Company" : "Black Data Processing Associates", "Role": "Technical Instructor", "JobDescription": ['Demonstrated an exceptional ability to teach and communicate complex coding concepts to students of varying skill levels, resulting in hihgly-engaged and knowledable learners.',
'Recreated popular website layouts with students by utilizing replit.com integrated development environment.']} ]
        data="Reginald Jean Amedee"
    elif fellow == "Cassey":
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

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
