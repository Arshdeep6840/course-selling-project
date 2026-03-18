#!/bin/sh

# Activate the virtual environment
source .venv/bin/activate

# Set the python path to include the project root
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run the flask app
.venv/bin/python -u -m flask --app main run --debug -p 8081