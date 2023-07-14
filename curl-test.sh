!#/bin/bash

curl --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=Malenia&email=theSevered&content=Just added database to my website!'

curl --request GET http://127.0.0.1:5000/api/timeline_post


