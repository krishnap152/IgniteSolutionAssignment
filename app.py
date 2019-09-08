from flask import Flask, render_template, request
import feedparser
import requests
from flask import make_response
from datetime import datetime, timedelta
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY   

def get_news(url):
    feed = feedparser.parse(url)
    articles = feed['entries']
    return articles

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            articles = get_news(url)   
        except:
            return render_template('index.html')
        if url:     
            response = make_response(render_template("index.html",
                articles=articles))
            expires = datetime.now() + timedelta(days=3)
            response.set_cookie("url", url, expires=expires)
            return response
        else:
            return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = False)
