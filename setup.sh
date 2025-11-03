#!/bin/bash

sudo apt-get update -y
sudo apt-get install python3-pip python3-venv

cd ..

python -m venv ~/PJAS

~/PJAS/bin/python -m pip install -r ~/PJAS/requirements.txt

cd PJAS
