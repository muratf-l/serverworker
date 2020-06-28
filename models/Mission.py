import datetime
from mongoengine import *


class Mission(Document):
    meta = {'collection': 'ZMission', 'strict': False}

    date_created = DateTimeField(default=datetime.datetime.utcnow)

    mission_id = StringField()

    # 10- vip, 20-manager, 0-all
    acc_type = IntField()

    acc_id = StringField()

    mission_title = StringField()

    mission_body = StringField()

    mission_completed = BooleanField()

    mission_completed_date = DateTimeField(default=datetime.datetime.utcnow)

    is_send = BooleanField()

    is_publish = BooleanField()

    count_completed = IntField()

    count_publish = IntField()

    creator_acc_id = StringField()

    creator_acc_type = IntField()
