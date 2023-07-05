#!/bin/bash

tmux kill-session
cd pe-portfolio-site-project-fork
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s auto
tmux send-keys -t auto "python -m venv python3-virtualenv" ENTER
tmux send-keys -t auto "source python3-virtualenv/bin/activate" ENTER
tmux send-keys -t auto "pip install -r requirements.txt" ENTER
tmux send-keys -t auto "flask run --host=0.0.0.0" ENTER
tmux send-keys -t auto "echo 'testing123'" ENTER
