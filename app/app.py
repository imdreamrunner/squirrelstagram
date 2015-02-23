import logging
from flask import Flask
from . import config

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
app = Flask(__name__)


@app.before_first_request
def create_db():
    from models import db, Media
    db.connect()
    db.create_tables([Media], True)


@app.before_request
def connect_db():
    from models import db
    db.connect()


@app.teardown_request
def disconnect_db(exc):
    from models import db
    if not db.is_closed():
        db.close()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def test():
    log.info("Testing")
    from . import insta
    media_list, max_tag_id = insta.get_media_list_by_tag("squirrel")
    for media in media_list:
        print(media.to_json())
        media.save(force_insert=True)
    return max_tag_id
