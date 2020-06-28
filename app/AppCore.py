import json

from app.helpers import logger

log = logger.get_logger('app')


class Manager:
    def __init__(self):
        self.config = {}

    @staticmethod
    def log_screen(cc, section, data=None):
        if data is None:
            log.info("%s : %s" % (cc, section))
        else:
            log.info("%s : %s : %s" % (cc, section, data))

    @classmethod
    def config_load(self, mode):
        config_file = ""

        if mode == "dev":
            config_file = "config_dev.json"
        else:
            config_file = "config_pro.json"

        with open(config_file, 'r') as f:
            try:
                instance.config = json.load(f)

                if mode == "dev":
                    instance.config["DEBUG"] = True
                else:
                    instance.config["DEBUG"] = False

                instance.config["MODE"] = mode

                from mongoengine import connect

                connect(
                    host=instance.config['MONGODB']
                )

                user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                instance.config["HEADERS"] = {'User-Agent': user_agent}

            except Exception as e:
                instance.config = {}
                log.error("Config Load Error: %s" % e)


instance = Manager()
