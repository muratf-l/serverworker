#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from app.AppCore import instance
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

application = Flask(__name__, template_folder="views")


def create_app():
    import os
    application.secret_key = os.urandom(24)
    application.url_map.strict_slashes = False

    from werkzeug.middleware.proxy_fix import ProxyFix
    application.wsgi_app = ProxyFix(application.wsgi_app, x_proto=1, x_host=1)

    register_blueprints()
    return application


def register_schedulers():
    scheduler = BackgroundScheduler()

    from app.jobs.job_mail_quee import job_mail_quee
    scheduler.add_job(job_mail_quee, trigger='interval', seconds=30, id='check_mail_que', max_instances=1)

    from app.jobs.job_mission_publish import job_mission_publish
    scheduler.add_job(job_mission_publish, trigger='interval', seconds=45, id='check_missions', max_instances=1)

    scheduler.start()
    return


def register_blueprints():
    from app.HomeController import home
    application.register_blueprint(home)
    return


@application.errorhandler(Exception)
def http_error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.code
    return response


@application.context_processor
def inject_stage_and_region():
    import datetime
    now = datetime.datetime.now()

    from app.AppCore import instance
    return dict(now=now.year, is_debug=instance.config["DEBUG"])


if __name__ == '__main__':
    LOG_CLASS = 'Cankan Worker'

    args = sys.argv

    if len(args) < 2:
        instance.log_screen(LOG_CLASS, 'main', 'Invalid Args (dev,pro): %s' % args)
        sys.exit()

    instance.config_load(args[1])

    instance.log_screen(LOG_CLASS, 'Worker version: %s %s port: %i' % (
        instance.config['VERSION'], instance.config['MODE'], instance.config['PORT']),
                        None)

    create_app()

    if instance.config["DEBUG"] is True:
        # -----------------------------------------------------------------------------------
        #

        # from app.jobs.job_mail_quee import job_mail_quee
        # job_mail_quee()

        # from app.jobs.job_mission_publish import job_mission_publish
        # job_mission_publish()

        #
        # -----------------------------------------------------------------------------------

        application.run(
            debug=True,
            host="0.0.0.0",
            port=instance.config['PORT']
        )
    else:
        register_schedulers()

        from gevent.pywsgi import WSGIServer

        http_server = WSGIServer(('', instance.config['PORT']), application)
        http_server.serve_forever()
