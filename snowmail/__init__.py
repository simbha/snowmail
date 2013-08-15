import os
import time
from flask import Flask, redirect, request, url_for, render_template, \
    send_from_directory, session
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views')
app = Flask(__name__, template_folder=tmpl_dir)
# app.config.update(DEBUG=True,)
# app.secret_key = settings.secret_key



# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(
#         app.root_path, 'static'), 'ico/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return redirect(url_for('login.index'))

# @app.route('/test')
# def test():
#     return render_template('test.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     errors = []
#     if request.method == 'POST' and 'email' in request.form:
#         form_errors = collect_form_errors(request.form)
#         if not form_errors:
#             email = request.form.get('email')
#             password = request.form.get('password')
#             conn, cur = get_sql()
#             cur.execute("""SELECT * FROM user WHERE email = '%s'
# AND password='%s'""" % (email, password))
#             res = cur.fetchall()
#             if not res:
#                 errors.append("email or password")
#             else:
#                 session['logged_in'] = True
#                 session['current_user'] = email
#                 cur.execute("""UPDATE user
# SET last_login=%s
# WHERE email=%s""", (int(time.time()), email))
#                 conn.commit()
#                 return redirect(url_for('newsletters.index'))
#     return render_template('auth/login.html', form_errors=errors)


# @app.route('/logout')
# @login_required
# def logout():
#     session['logged_in'] = False
#     session['current_user'] = ''
#     return render_template('auth/login.html', logout=True)