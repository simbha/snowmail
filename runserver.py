from snowmail import app
from snowmail.controllers import login, messages

#application = app

if __name__ == '__main__':
    app.register_blueprint(login.mod)
    app.register_blueprint(messages.mod)
    app.run(host='0.0.0.0', port=5000, debug=True)