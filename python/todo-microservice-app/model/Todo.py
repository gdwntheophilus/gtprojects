from utils.date_time_util import uuid_from_string , format_timestamp
from datetime import datetime
import time

class Todo(object):

    def __init__(self,todoDate,todoDesc,todoName):
        self.todoDate = format_timestamp(todoDate)
        self.todoDesc = todoDesc
        self.todoName = todoName
        self.todoUid = uuid_from_string('data')

    def setTodoDate(self,todoDate):
        self.todoDate = todoDate
    def setTodoDesc(self,todoDesc):
        self.todoDesc = todoDesc
    def setTodoName(self,todoName):
        self.todoName = todoName
    def setTodoUuid(self,todoUuid):
        self.todoUid = todoUuid
    def getTodoName(self):
        return self.todoName
    def getTodoDesc(self):
        return self.todoDesc
    def getTodoDate(self):
        return self.todoDate
    def getTodoUuid(self):
        return self.todoUid
    def toString(self):
        print(
            'Todo[ todoDate={todoDateVar},todoDesc={todoDescVar},todoName={todoNameVar},todoUid={todoUidVar} ]'.format(
                todoDateVar=self.todoDate,
                todoDescVar=self.todoDesc,
                todoNameVar=self.todoName,
                todoUidVar=self.todoUid
                )
            )
