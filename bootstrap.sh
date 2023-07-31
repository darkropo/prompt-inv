#!/bin/bash
source /home/darkropo/Develops/prompt-inv/venv/bin/activate
export FLASK_APP=./promptinv/src/index.py
pipenv run flask run -h 0.0.0.0