
from flask import Blueprint, request
from flask_cors import CORS

from service.AstraService import astra_service

todo_controller = Blueprint('todo_controller',__name__)

CORS(todo_controller)

@todo_controller.route("/save",methods = ['GET'])
def saveTodo():
    print(request.content_type)
    if request.content_type == 'application/json':
        astra_service.getSaveTodoDAO(request.json['todoDate'],request.json['todoDesc'],request.json['todoName'])
        return request.json