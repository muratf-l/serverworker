def get_ip(ipStr):
    if 'tcp' in ipStr:
        return ipStr.split(':')[1]

    return ipStr


def parse_dynamic_data(s: str):
    if s is None:
        return None

    import urllib.parse
    c_data = urllib.parse.unquote(s)

    if c_data is None:
        return None

    import json
    o = json.loads(c_data)

    return o
