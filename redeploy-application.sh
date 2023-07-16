#!/bin/bash

cd /root/pe-portfolio-site-project 

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt


