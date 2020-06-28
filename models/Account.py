from mongoengine import *


class Account(Document):
    meta = {'collection': 'ZAccounts', 'strict': False}

    _id = ObjectIdField()

    acc_type = IntField()
    acc_parent_id = StringField()
    acc_email = StringField()
    acc_guid = StringField()
    acc_confirmed = BooleanField()
