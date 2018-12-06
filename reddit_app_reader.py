from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_headlines():
    user_pass_dict = {'user': 'edmacker',
                      'passwd': '2015AsdfLkjhReddit',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Hi I am testing Alexa: edmacker'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/spacex/.json?limit=15'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([i for i in titles])
    return titles

def get_loungeheadline():
    user_pass_dict = {'user': 'edmacker',
                      'passwd': '2015AsdfLkjhReddit',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Hi I am testing Alexa: edmacker'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/SpaceXLounge/.json?limit=15'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([i for i in titles])
    return titles

def get_pythonheadline():
    user_pass_dict = {'user': 'edmacker',
                      'passwd': '2015AsdfLkjhReddit',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Hi I am testing Alexa: edmacker'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    url = 'https://reddit.com/r/python/.json?limit=15'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([i for i in titles])
    return titles

#This will test our code
#titles = get_headlines()
#print(titles)

@app.route('/')
def homepage():
    return "hi mr coder, how ya doing?"

@ask.launch
def start_skill():
    welcome_message = 'Hello Dougie Doo, would you like to hear some reddit news about SpaceX...Python...or SpaceXLounge? For SpaceX just say Yes, for Python say Python...and...for SpaceXLounge please say Another.'
    return question(welcome_message)

@ask.intent("PythonIntent")
def share_pythonheadline():
    pythonheadline = get_pythonheadline()
    pythonheadline_msg = 'Todays current Python news headlines from reddit are  {}'.format(pythonheadline)
    return statement(pythonheadline_msg)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'Todays current SpaceX news headlines from reddit are  {}'.format(headlines)
    return statement(headline_msg)

@ask.intent("LoungeIntent")
def share_loungeheadline():
    loungeheadline = get_loungeheadline()
    loungeheadline_msg = 'Todays current SpaceXLounge news headlines from reddit are  {}'.format(loungeheadline)
    return statement(loungeheadline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Ok, thats fair...just let me know when you would like to try again. Bye Bye for now!'
    return statement(bye_text)

if __name__ == '__main__':
    app.run(debug=True)
