
from abc import abstractmethod


class Task(object):
    
    def __init__(self):
        self._next = None
        self._taskHandler = None
        self._params = dict()
        self._exceptionThrown = False
    
    @abstractmethod
    def run(self):
        pass
    
    @property
    def taskHandler(self):
        return self._taskHandler
    
    @taskHandler.setter
    def taskHandler(self, taskHandler):
        if not (self._taskHandler):
            self._taskHandler = taskHandler

    @property
    def exceptionThrown(self):
        return self._exceptionThrown
    
    @exceptionThrown.setter
    def exceptionThrown(self, isThrown):
        self._exceptionThrown = isThrown

    @property
    def next(self):
        self._next.params.update(self.params)
        return self._next
    
    @next.setter
    def next(self, task):
        if (task):
            task.params.update(self.params)
            self._next = task
        
    def hasNextChild(self):
        return self._taskHandler.hasMoreSubTask()
    
    def getNextChild(self):
        child = self._taskHandler.getNextSubTask()
        child.params.update(self.params)
        return child

    @property
    def params(self):
        return self._params
    
    @params.setter
    def params(self, params):
        self._params.update(params)
