import os
import json

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


BASIC = json.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/basic.json")), "r"))
AUTH = json.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), "../config/auth.json")), "r"))
