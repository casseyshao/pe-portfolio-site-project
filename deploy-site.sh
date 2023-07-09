#!/bin/bash


if tmux list-sessions >/dev/null 2>&1; then
    tmux kill-server
fi


cd "pe-portfolio-site-project"
echo "$PWD"

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt


if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Python virtual environment is active."
else
    echo "Python virtual environment is not active."
fi

tmux new-session -d -s deploy


if tmux has-session -t 'deploy' >/dev/null 2>&1; then
    echo "Tmux session 'deploy' is active."
else
    echo "Tmux session 'deploy' is not active."
fi

flask run --host=0.0.0.0