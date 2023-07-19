#!/bin/bash

# Should create a random timeline post using POST and check GET to make sure it was added.

# New timeline post
name='Cassey'
email='cassey@test.com'
content='Testing'

ADDNEW=$(curl --request POST http://localhost:5000/api/timeline_post -d 'name=Cassey&email=cassey@test.com&content=Testing')
echo "$ADDNEW"
RESULTS=$(curl http://localhost:5000/api/timeline_post)

value=$( jq --null-input --raw-output --arg newName "$name" --arg newEmail "$email" --arg newContent "$content"\
        "$RESULTS"' | .timeline_posts[] | select(.name == $newName and .email == $newEmail and .content == $newContent) | .content')
echo "$value"
if [ "$value" == "" ]; then
    echo "Did not add successfully"
else
    echo "Added successfully"
fi
