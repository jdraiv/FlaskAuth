
from flask import Flask

app = Flask(__name__)


app.config.update(
    DEBUG=True,
    SECRET_KEY='notasecretkey'
)


import views
import auth.routes