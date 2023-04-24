from app.forms import LoginForm
from flask import Flask
from flask import render_template
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
@app.route('/')
@app.route('/index')
@app.route('/login')
def index():  # put application's code here
    user = {'username':'crazy'}
    posts =[{
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }]
    return render_template('index.html',title='home',user=user,posts=posts)
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)



