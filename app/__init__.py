import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
hobbyImageDir = os.path.join('img')
img = os.path.join('static', 'img')

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


pic_data = {
"Reginald Amedee": "./static/img/reginald.jpeg",
"Eyob Dagnachew": "./static/img/eyob.jpeg",        
"Cassey Shao": "./static/img/cassey.JPG",
}


about_me= {

    "Reginald Amedee": """About Me: Hi, My name is Reginald and I am a developer based out 
    of New York City. I have three years of Account Management/Customer Success experience 
    in technology. I've always wanted to bo be an engineer and made 
    the courageous decision to quit my job last 
    year to pursue this passion full time! 
    I have experience with a variety of technologies and 
    I love to build things. Always looking to collaborate!""",

    "Cassey Shao": """ About me: Hi my name is Cassey! I am a new grad computer engineering student
    from University of Toronto! I am interested in building good software! 
    I have experience with building software from school, internships, and hackathons! 
    Outside of this, I love being active! I like hiking, going on long walks in downtown, and playing sports!""",

    "Eyob Dagnachew": """Hello there! My name is Eyob, I'm an incoming junior at 
    Carnegie Mellon University in Pittsburgh! I love trying to find new ways to apply creativity
    to make something new in the world! One of those ways is through coding which is something I've
    been doing for the past couple years through internships, research, and hackathons! other than tech
    I'm usually trying to find some more artistic outlets for my creativity, resulting in me
    having a camera bag, sketchbook and laptop in my backpack almost constantly!  """
}

@app.route('/')
def index():

    intro_message = "Welcome to our page! Click on a fellow to learn more about them!"
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), landing_data=landing_data, intro_message=intro_message)

@app.route('/<fellow>')
def fellowPage(fellow):
    full_name = fellow.split()
    image_link = full_name[0]
    
    fellow=request.args.get('fellow', fellow)
    print()
    return render_template('aboutMePage.html', fellow=fellow, name= image_link, data= pic_data, intro= about_me)

@app.route('/<fellow>/experience')
def experiencePage(fellow):
    if fellow == "Reginald Amedee":
        experience=[{"Company" : "Vimeo", "Role": "Account Manager", "JobDescription": ['Recommended brand products to customers, highlighted benefits and redirected objections to secure more than $1,000,000 in upsell.',
'Worked in an agile environment with Technical Program Managers to ensure that Vimeo’s services are correctly implemented at deadlines that are set.'], 'Date': "Aug 2019 - Feb 2022"},{"Company" : "AFreeBird.org", "Role": "Web Enigneer", "JobDescription": ['Making website more responsive on various screen sizes.',
'Lead Developer on a proprietary solution that will save over $5000 a year', 'Built out database models and backend using Django and Python according to system design requirements.'], "Date": "Feb 2023 - June 2023"}, {"Company" : "B.D.P.A", "Role": "Technical Instructor", "JobDescription": ['Demonstrated an exceptional ability to teach and communicate complex coding concepts to students of varying skill levels, resulting in hihgly-engaged and knowledable learners.',
'Recreated popular website layouts with students by utilizing replit.com integrated development environment.'], "Date": "Feb 2023 - Aug 2023"}]
        data="Reginald Amedee"
    elif fellow == "Cassey Shao":
        experience=[{"Company" : "Amazon", "Role": "Software Engineer Intern", "JobDescription": ['Designed and worked on a command line tool to automate calculating Time-to-FirstResponse metric information for resolver groups to track their performance with responding to external requests.',
'Abstracted models and encapsulated logic to future-proof the software and make it reusable by other teams', 'Wrote unit tests to test the functionality of the components in the command line tool.'], "Date": "May 2022 - Aug 2022"}, {"Company" : "University of Toronto", "Role": "Teaching Assistant", "JobDescription": ['Course: CSC343 Introduction to Databases',
'Department(Dept): Dept. of Computer Science', 'Answered questions and graded evaluations containing relational data model, database design, and SQL concepts.'], "Date": "Jan 2022 - May 2022"}]
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        experience=[{"Company" : "Fluence", "Role": "Data Science Modeling Intern", "JobDescription": ['Re-organized test scripts into implementation tests and behavior tests, and increased coverage of both categories of tests.',
'Implemented data pipeline for site-specific temperature and dispatch data from two sites.', 'Evaluated existing model performance against site data, and determined if there is site-specific bias in the existing model.', 'Implemented a Long-Short Term Model to improve prediction accuracy for individual sites'], "Date": 'June 2022 - Aug 2022'}]
        data="Eyob Dagnachew"

    return render_template('experiencePage.html', data=data, experience=experience)

@app.route('/<fellow>/hobbies')
def hobbiesPage(fellow):
    hobbyImage1=os.path.join(hobbyImageDir, 'elden_ring.png')
    hobbyImage2=os.path.join(hobbyImageDir, 'pic7.png')
    hikingImage=os.path.join(hobbyImageDir, "hiking.webp")
    bookImage=os.path.join(hobbyImageDir, "books.webp")
    travelImage=os.path.join(hobbyImageDir, "travel.jpg")
    eyobPhotography=os.path.join(hobbyImageDir, "eyobPhotography.webp")
    digitalArt=os.path.join(hobbyImageDir, "digitalArt.webp")
    lightWriting=os.path.join(hobbyImageDir, "lightWriting.avif")

    if fellow == "Reginald Amedee":
        data="Reginald Amedee"
        hobbies=[{"Hobby_Blurb" : "I love to play video games. My favorite genre of video games are RPGs. Currently playing Diablo 4. I am also on my third playthrough for Elden Ring!", "Hobby_Image": hobbyImage1},
                {"Hobby_Blurb": "I enjoy calisthenics, which is a form of exercise that prioritizes body movements such as push ups, sit ups, pull ups, etc... In fact, I love it so much that I created an app to track your calisthenics progressions and movements called StrengthTracker.", "Hobby_Image": hobbyImage2},]
    elif fellow == "Cassey Shao":
        data="Cassey Shao"
        hobbies=[{"Hobby_Blurb" : "I enjoy reading everything from non-fiction to novels to poems to plays and more! I made it a goal this year to read 12 books.", "Hobby_Image": bookImage},
                {"Hobby_Blurb": "I enjoy being outside and walking! One of my favourite hikes was Panorama Ridge in BC, Canada!", "Hobby_Image": travelImage}, {"Hobby_Blurb": "I love being on the road and having new experiences and trying new foods and meeting people! It is a dream to be able to travel a lot in my life!", "Hobby_Image": hikingImage}]
    elif fellow == "Eyob Dagnachew":
        hobbies=[{"Hobby_Blurb" : "I always enjoy putting something from my imagination and challenging myself into making it as real as possible with the basic theories of art.", "Hobby_Image": digitalArt},
                {"Hobby_Blurb": "I love photography because it challenges me to taking something that already exists that I already like and engage with it in a new way by trying to represent it in a new was through the lens.", "Hobby_Image": eyobPhotography}, {"Hobby_Blurb": "I like writing because it fills the gap of things that i cant bring to life in writing by brining them to life with my words instead, allowing me to delved even further to my imagination.", "Hobby_Image": lightWriting}]
        data="Eyob Dagnachew"

    return render_template('hobbiesPage.html', data=data, hobbies=hobbies)


@app.route('/<fellow>/education')
def education(fellow):
    if fellow == "Reginald Amedee":
        experience=[{"Company" : "St. John's University", "Role": "Bachelor's degree, English; Business & English;", 'Date': "2010 - 2015"},{"Company" : "Coding Dojo", "Role": "Activities and societies: Certificate of completion", "JobDescription": [' Worked on projects that included Techonologies such as HTML/HTML5, CSS, MERN Stack, and JavaScript'], "Date": "March 2021 - July 2021"}, {"Company" : "B.D.P.A", "Role": "Technical Instructor", "JobDescription": ['Demonstrated an exceptional ability to teach and communicate complex coding concepts to students of varying skill levels, resulting in hihgly-engaged and knowledable learners.',
'Recreated popular website layouts with students by utilizing replit.com integrated development environment.'], "Date": "Feb 2023 - Aug 2023"}]
        data="Reginald Amedee"
    elif fellow == "Cassey Shao":
        experience=[{"Company" : "University of Toronto", "Role": "BASc, Computer Enginnering", "JobDescription": ["Activities and societies: Skule Intramural Women's Ice Hockey 2022-2023 | Engineering Orientation Week Group Head Leader 2020 and 2022 | Computer Science PRISM (Preparation for Research through Immersion, Skills, and Mentorship) 2022 Cohort | Sustainable Engineers Association Co-President 2020-2021 | ILead Summer Fellows 2020 Cohort | Sustainable Engineers Association Awareness and Support Director 2019-2020",
'Candidate for computer engineering major, business minor, and artificial intelligence certificate. Enrolled in the Professional Experience Year (PEY) co-op program.'], "Date": "Sep 2018 - June 2023"}, {"Company" : "Etobicoke School of the Arts","Role": "High School Diploma, Contemporary Visual Arts", "JobDescription": ["Activities and societies: Student Council President (2017-2018)", "Equity Committee Co-President (2015-2018)", "Student Council Equity Representative (2015-2017) ", ],  "Date": "2014 - 2018"}]
        data="Cassey Shao"
    elif fellow == "Eyob Dagnachew":
        experience=[{"Company" : "Carnegie Mellon", "Role": "B.S in  Statistics/Machine Learning","JobDescription": ["Relevent Coursework: Data Structures and Algorithms, Fundamentals of Software Engineering , Methods for Statistics and Data Science, Probability and Statistical Inference, Concepts of Mathematics"],

 "Date": 'June 2021 - May 2025'},
                    {"Company" : "Annandale High School", "Role": "IB Diploma ","Date" : " August 2017 - May 2021"}]
        data="Eyob Dagnachew"


    return render_template('education.html', data = data, experience = experience)
