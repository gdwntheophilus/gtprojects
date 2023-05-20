
from uuid import UUID
import uuid
from datetime import datetime

def uuid_from_string(string):
    return uuid.uuid1()
    # return UUID('{s}'.format(s=string))

def format_timestamp(string):
    if isinstance(string,str):
        return datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
    if isinstance(string,datetime):
        return string