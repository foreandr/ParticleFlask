import os
from flask import Flask, render_template, request, session, redirect,  url_for, g


TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')
# import sql_functions

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'demokey'

username = ''

# user = sql_functions.check_users() #list of user in DB

@app.route('/', methods = ['GET']) # homepage
def home():
    print('EXECUTING HOME FUNCTION')
    return render_template('index.html', message="index.html page")

@app.route('/blog', methods = ['GET']) # homepage
def blog():
    print('EXECUTING BLOG FUNCTION')
    return render_template('blog.html', message="blog.html page")

@app.route('/blog', methods = ['GET']) # homepage
def code():
    print('EXECUTING BLOG FUNCTION')
    return render_template('code.html', message="code.html page")

if __name__ == '__main__':
    my_port = 5006
    app.run(host = 'localhost', port = my_port, debug = True) # host is to get off localhost
    # If the debugger is on, I can change my files in real time after saving