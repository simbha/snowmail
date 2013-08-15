from flask import Blueprint, request, redirect, url_for, \
    render_template, session

mod = Blueprint('login', __name__)


@mod.route('/login')
def index():
    return render_template('login/index.html')