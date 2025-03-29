from flask import Flask

app = Flask(__name__)

# this import must happen below app instance
from program import routes
