@echo off

:start
cls

rem install requirements in python 
pip install -r requirements.txt
cls rem clear existing output

rem start cmd with current folder and run script
python gen.py
