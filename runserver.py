from snowmail import app
from snowmail.controllers import login, dashboard

#application = app

if __name__ == '__main__':
    app.register_blueprint(login.mod)
    app.register_blueprint(dashboard.mod)
    app.run(host='0.0.0.0', port=5000, debug=True)