from flask import Flask
from routes import *
from uploads import *
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()  