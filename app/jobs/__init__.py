


def add_response(response, url):
    from models.WorkLog import WorkLog
    workLog = WorkLog()
    workLog.r_code = response.status_code
    workLog.r_content = response.text
    workLog.r_link = url
    workLog.save()
