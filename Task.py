from abc import abstractmethod

class Task(object):
    
    def __init__(self):
        self._next = None
        self.params = dict()
    
    @abstractmethod
    def run(self):
        pass

    def getNextTask(self):
        return None
        
    def hasNextChild(self):
        return False
    
    def getNextChild(self):
        return None


class TaskExecutionException(Exception):
    def __init__(self, message):
        super().__init__(message + " has thrown an execution exception.")
