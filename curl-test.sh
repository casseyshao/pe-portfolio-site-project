#!/bin/bash

LIST=$(curl  http://localhost:5000/api/timeline_post)


ENTRY_COUNT=$(echo "$LIST" | jq '.timeline_posts | length')


echo "this is a test  $ENTRY_COUNT"
# Example command to list files
if [ $LIST -ne 400 ]; then
    echo "Command ran successfully"
else
    echo "Command encountered an error"
fi


curl --request POST http://localhost:5000/api/timeline_post -d 'name=test&email=test@gmail.com&content=just added a database'

LIST2=$(curl  http://localhost:5000/api/timeline_post)
ENTRY_COUNT2=$(echo "$LIST2" | jq '.timeline_posts | length')



if [ $ENTRY_COUNT2 -eq  $((ENTRY_COUNT+1)) ]; then
	echo "Get request works"

else
	echo "Get request failure"
fi


