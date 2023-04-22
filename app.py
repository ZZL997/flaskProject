from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():  # put application's code here
    user = {'username':'crazy'}
    return render_template('page1.html',title='home',user=user)

if __name__ == '__main__':
    app.run()
