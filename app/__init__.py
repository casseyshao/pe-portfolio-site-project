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
'Worked in an agile environment with Technical Program Managers to ensure that Vimeo’s services are correctly implemented at deadlines that are set.'], 'Date': "Aug 2019 - Feb 2022"},{"Company" : "AFreeBird.org", "Role": "Web Enigneer", "JobDescription": ['Making website more responsive on various screen sizes.',
'Lead Developer on a proprietary solution that will save over $5000 a year', 'Built out database models and backend using Django and Python according to system design requirements.'], "Date": "Feb 2023 - June 2023"}, {"Company" : "B.D.P.A", "Role": "Technical Instructor", "JobDescription": ['Demonstrated an exceptional ability to teach and communicate complex coding concepts to students of varying skill levels, resulting in hihgly-engaged and knowledable learners.',
'Recreated popular website layouts with students by utilizing replit.com integrated development environment.'], "Date": "Feb 2023 - Aug 2023"}]
        data="Reginald Jean Amedee"
    elif fellow == "Cassey":
        experience=[{"Company" : "Amazon", "Role": "Software Development Engineer Intern", "JobDescription": ['Designed and worked on a command line tool to automate calculating Time-to-FirstResponse metric information for resolver groups to track their performance with responding to external requests.',
'Abstracted models and encapsulated logic to future-proof the software and make it reusable by other teams', 'Wrote unit tests to test the functionality of the components in the command line tool.'], "Date": "May 2022 - Aug 2022"}, {"Company" : "University of Toronto", "Role": "Teaching Assistant", "JobDescription": ['Course: CSC343 Introduction to Databases',
'Department(Dept): Dept. of Computer Science', 'Answered questions and graded evaluations containing relational data model, database design, and SQL concepts.'], "Date": "Jan 2022 - May 2022"}]
        data="Cassey Shao"
    elif fellow == "Eyob":
        experience=[{"Company" : "Fluence", "Role": "Data Science Modeling Intern", "JobDescription": ['Re-organized test scripts into implementation tests and behavior tests, and increased coverage of both categories of tests.',
'Implemented data pipeline for site-specific temperature and dispatch data from two sites.', 'Evaluated existing model performance against site data, and determined if there is site-specific bias in the existing model.', 'Implemented a Long-Short Term Model to improve prediction accuracy for individual sites'], "Date": 'June 2022 - Aug 2022'}]
        data="Eyob Dagnachew"

    return render_template('experiencePage.html', data=data, experience=experience)

@app.route('/<fellow>/hobbies')
def hobbiesPage(fellow):
    hobbyImage1=os.path.join(hobbyImageDir, 'elden_ring.png')
    hobbyImage2=os.path.join(hobbyImageDir, 'reggie_picture.jpg')
    hikingImage=os.path.join(hobbyImageDir, "hiking.webp")
    bookImage=os.path.join(hobbyImageDir, "books.webp")
    travelImage=os.path.join(hobbyImageDir, "travel.jpg")

    if fellow == "Reginald":
        data="Reginald Jean Amedee"
        hobbies=[{"Hobby_Blurb" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.", "Hobby_Image": hobbyImage1},
                {"Hobby_Blurb": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.", "Hobby_Image": hobbyImage2},]
    elif fellow == "Cassey":
        data="Cassey Shao"
        hobbies=[{"Hobby_Blurb" : "I enjoy reading everything from non-fiction to novels to poems to plays and more! I made it a goal this year to read 12 books.", "Hobby_Image": bookImage},
                {"Hobby_Blurb": "I enjoy being outside and walking! One of my favourite hikes was Panorama Ridge in BC, Canada!", "Hobby_Image": travelImage}, {"Hobby_Blurb": "I love being on the road and having new experiences and trying new foods and meeting people! It is a dream to be able to travel a lot in my life!", "Hobby_Image": hikingImage}]
    elif fellow == "Eyob Dagnachew":
        data="Eyob Dagnachew"

    return render_template('hobbiesPage.html', data=data, hobbies=hobbies)
