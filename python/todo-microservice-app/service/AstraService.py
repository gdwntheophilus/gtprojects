
from dao import SaveTodoDao
class AstraService(object):
    saveTodoDao = None
    def getSaveTodoDAO(self,todoDate,todoDesc,todoName):
        if self.saveTodoDao == None:
            save_to_do = SaveTodoDao.SaveTodoDao()
            print("----------------------------------------")
            save_to_do.write_to_do(todoDate,todoDesc,todoName)

astra_service = AstraService()