from abc import abstractmethod
from bingdog.Util import ExtProcessShellUtil
class Task(object):
    
    def __init__(self, taskId):
        self.params = dict()
        self.statement = None
        self._taskId = taskId
    
    @property
    def taskId(self):
        return self._taskId
    
    @abstractmethod
    def run(self):
        pass

    def getNextTask(self):
        return None
        
    def hasNextChild(self):
        return False
    
    def getNextChild(self):
        return None
        
    def _processStatement(self,statement):
        if (statement):
            for key in self.params:
                statement = statement.replace(key, self.params[key])
            return statement
        else:
            return None

class ShellExecutionTask(Task):
    def __init__(self, taskId):
        super().__init__(taskId)
        self._extUtil = ExtProcessShellUtil()
    
    def run(self):
        self._extUtil.execute(self._processStatement(self.statement))

class TaskExecutionException(Exception):
    def __init__(self, message):
        super().__init__(message + " has thrown an execution exception.")
