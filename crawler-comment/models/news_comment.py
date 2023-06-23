from array import array
from mongoengine import *
from datetime import datetime
from bson import ObjectId

class sub_comment(EmbeddedDocument):
    _id = ObjectIdField()
    content = StringField()
    reaction = StringField()

class news_comment(Document):
    _id = ObjectIdField()
    content = StringField()
    reaction = StringField()
    subcomments = EmbeddedDocumentListField(sub_comment)
    meta = {'collection': 'news_comment'}
    @classmethod
    def post_save(cls, sender, document, **kwargs):
        print(document._id)
