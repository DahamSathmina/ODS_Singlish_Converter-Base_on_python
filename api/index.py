from flask import Flask, render_template

# Tell Flask where to find templates (one folder up)
app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

# Required by Vercel to handle WSGI
def handler(environ, start_response):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.wrappers import Request, Response

    application = DispatcherMiddleware(app)
    return application(environ, start_response)
