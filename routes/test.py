
from . import routes
import os
@routes.route("/testapi1", methods=['POST'])
def home1():
    return os.getcwd()