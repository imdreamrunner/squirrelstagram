import os
import logging
from peewee import SqliteDatabase, Model, CharField, DateTimeField

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"

log = logging.getLogger(__name__)
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../store.db"))
log.info("Database path " + db_path)
db = SqliteDatabase(db_path, threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = db


class Media(BaseModel):
    id = CharField(primary_key=True)
    user = CharField()
    created_time = DateTimeField()
    caption = CharField()
    tags = CharField()
    type = CharField()
    images = CharField()
    videos = CharField(null=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "created_time": self.created_time,
            "caption": self.caption,
            "tags": self.tags,
            "type": self.type,
            "images": self.images,
            "videos": self.videos
        }

    def to_json(self):
        package = {
            "id": self.id,
            "user": self.user,
            "created_time": self.created_time.strftime("%Y-%m-%d %H:%M:%S"),
            "caption": self.caption,
            "tags": self.tags,
            "type": self.type,
            "images": self.images,
            "videos": self.videos
        }
        import json
        return json.dumps(package)

