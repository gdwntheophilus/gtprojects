from flask import Flask
from flask_cors import CORS
from controller.Todo import todo_controller

app = Flask(__name__)

CORS(app)
app.register_blueprint(todo_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)