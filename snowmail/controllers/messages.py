from flask import Blueprint, request, redirect, url_for, \
    render_template, session

mod = Blueprint('messages', __name__)


def index():
    
    return render_template('messages/index.html')