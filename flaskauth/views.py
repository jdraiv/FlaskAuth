

from flaskauth import app


@app.route('/')
def homepage():
    return 'Homepage'