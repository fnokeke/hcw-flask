from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

import hcw_flask.views
import hcw_flask.models
