from flask import Blueprint, request, redirect, url_for, \
    render_template, session

mod = Blueprint('dashboard', __name__)


def index():
    return render_template('dashboard/index.html')