import datetime
from mongoengine import *

from app.helpers.mailUtil import send_mail


def job_mission_publish():
    print("job_mission_publish")

    from models.Mission import Mission
    from models.Account import Account

    mission_list = Mission.objects(is_publish=True, is_send=False)

    for row in mission_list:
        account_list = None

        if row.acc_type == 0 and row.creator_acc_type == 20:
            account_list = Account.objects(acc_parent_id=row.creator_acc_id, acc_confirmed=True)

        if row.acc_type == 0 and row.creator_acc_type == 30:
            account_list = Account.objects(acc_type__ne=30, acc_confirmed=True)

        if row.acc_type == 20 and row.creator_acc_type == 30:
            account_list = Account.objects(acc_type=20, acc_confirmed=True)

        for account in account_list:
            mission = Mission()
            mission.mission_id = str(row.id)
            mission.acc_id = str(account._id)
            mission.mission_title = row.mission_title
            mission.mission_body = row.mission_body
            mission.mission_completed = False
            mission.mission_completed_date = None
            mission.is_publish = True
            mission.is_send = True
            mission.save()

            from AppRun import application
            template = application.jinja_env.get_or_select_template("templates/acc_mission.html")

            context = {
                'link': "request.host_url"
            }

            from models.MailQue import MailQue

            MailQue.add_quee(
                acc_id=str(account._id),
                body=template.render(context),
                subject="Cankan VIP için yeni bir görevin var",
                to=account.acc_email
            )

        row.is_send = True
        row.count_publish = account_list.count()
        row.save()

    print("job_mission_publish OK!")
