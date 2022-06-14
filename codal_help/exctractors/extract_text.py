import re
import json

def extract_datasource(html):
    str_datasource = re.findall("var datasource = (.*?)};", html)
    if len(str_datasource):
        return json.loads(str_datasource[0] + "}")
    else:
        raise Exception("datasource is not exist.")