#!/usr/bin/env bash

#Environment name
VENVNAME=as4env

#Activate environment
source $VENVNAME/bin/activate

#Upgrade pip
pip install --upgrade pip

# problems when installing from requirements.txt
test -f requirements.txt && pip install -r requirements.txt

#navigate to src folder
cd src

#run script
python3 lr-mnist.py $@
python3 nn-mnist.py $@

#deactivate environment
deactivate
