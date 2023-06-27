import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium

load_dotenv()
app = Flask(__name__)
hobbyImageDir = os.path.join('img')
img = os.path.join('static', 'img')

# Landing page data
landing_data = [
    {
        "name": "Reginald Amedee",
        "img": "./static/img/reginald.jpeg",
        "marker_color": "green",
        "places": [
            {
                "coord": [43.6532, -79.3832],
                "name": "Toronto"
            },
            {
                "coord": [37.4415, 25.3667],
                "name": "Mykonos"
            },
            {
                "coord": [23.1136, -82.3666],
                "name": "Cuba"
            },
            {
                "coord": [10.6918, -61.2225],
                "name": "Trinidad"
            },
            {
                "coord": [36.3932, 25.4615],
                "name": "Santorini"
            },
            {
                "coord": [64.9631, -19.0208],
                "name": "Iceland"
            },
            {
                "coord": [18.1096, 77.2975],
                "name": "Jamaica"
            }
        ],
    },
    {
        "name": "Eyob Dagnachew",
        "img": "./static/img/eyob.jpeg",
        "marker_color": "red",
        "places": [
            {
                "coord": [43.7615, -79.4111],
                "name": "Canada"
            },
            {
                "coord": [9.1450, 40.4897],
                "name": "Ethiopia"
            },
            {
                "coord": [52.3555, -1.1743],
                "name": "England"
            }
        ],
    },
    {
        "name": "Cassey Shao",
        "img": "./static/img/cassey.JPG",
        "marker_color": "blue",
        "places": [
            {
                "coord": [43.6205, -79.5132],
                "name": "Toronto"
            },
            {
                "coord": [48.8566, 2.3522],
                "name": "Paris"
            },
            {
                "coord": [38.7223, 9.1393],
                "name": "Lisbon"
            },
            {
                "coord": [43.7696, 11.2558],
                "name": "Florence"
            },
            {
                "coord": [37.9838, 23.7275],
                "name": "Athens"
            },
            {
                "coord": [39.9042, 116.4074],
                "name": "Beijing"
            },
            {
                "coord": [22.5090, -78.4070],
                "name": "Cayo Coco"
            }
        ],
    }
]

def build_map():
    my_map = folium.Map()

    # Add markers for each person
    for person in landing_data:
        for p in person["places"]:
            folium.Marker(p["coord"], popup = p["name"], icon=folium.Icon(color=person["marker_color"], icon="check")).add_to(my_map)

    my_map = my_map._repr_html_()
    return my_map

@app.route('/')
def index():
    my_map = build_map()
    intro_message = "Welcome to our page! Click on a fellow to learn more about them!"
    map_title = "A map of all the places that we have been to:"
    map_desc = "Reginald (Green), Eyob (Red), Cassey (Blue)"
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), landing_data=landing_data, intro_message=intro_message, my_map=my_map, map_title=map_title, map_desc=map_desc)

@app.route('/<fellow>')
def fellowPage(fellow):
    fellow=request.args.get('fellow', fellow)
    return render_template('aboutMePage.html', fellow=fellow)

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


