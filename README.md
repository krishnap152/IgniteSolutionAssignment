# IgniteSolutionAssignment

Steps to run the application

1. Need to install packages from requirements.txt
    a) command to install 
    pip install -r requirements.txt

2. To run web app
    b) command to run web app
    gunicorn -w 3 app:app gevent --worker-connections 1000