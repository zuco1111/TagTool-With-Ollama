@echo off

python -m venv venv

call venv\Scripts\activate

pip install requests


echo Virtual environment and dependencies setup complete.

pause
