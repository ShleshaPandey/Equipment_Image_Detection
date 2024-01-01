from flask import *
routes = Blueprint('routes', __name__)

from .test import *
from .obdet import *