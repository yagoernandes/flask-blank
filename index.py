from flask import Flask, request
app = Flask(__name__)

from routes.login import do_login, show_login_form


@app.route('/')
def index():
    return 'Online!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_login()
    else:
        return show_login_form()
