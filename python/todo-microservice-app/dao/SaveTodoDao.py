from model import Todo
from astra.AstraDB import AstraDBSession
class SaveTodoDao(object):

    table_name = "todo"
    save_todo_entry_stmt = 'insert into todokeyspace.{todo} (tododate,tododesc,todoname,todouuid) values(:tododate,:tododesc,:todoname,:todouuid)'.format(todo=table_name)

    def __init__(self):
        self.astraSession = AstraDBSession.getConnection()

        self.save_todo_entry_prep_stmt = self.astraSession.prepare(self.save_todo_entry_stmt)

    def write_to_do(self,todoDate,todoDesc,todoName):
        print('{},{},{}'.format(todoDate,todoName,todoDesc))
        todo_entry = Todo.Todo(todoDate=todoDate,todoDesc=todoDesc,todoName=todoName)
        print(todo_entry.toString())
        date = todo_entry.getTodoDate()
        desc = todo_entry.getTodoDesc()
        name = todo_entry.getTodoName()
        id = todo_entry.getTodoUuid()
        print('{},{},{},{}'.format(date,desc,name,id))
        query = self.save_todo_entry_prep_stmt.bind({
            'tododate':date,
            'tododesc':desc,
            'todoname':name,
            'todouuid':id
        })
        self.astraSession.execute_async(query)