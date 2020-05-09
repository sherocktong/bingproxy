from abc import abstractmethod
from bingdog.TaskDecorator import TaskDecorator

class Task(object):
    
    def __init__(self):
        self._next = None
        self._params = dict()
        self._exceptionThrown = False
    
    @abstractmethod
    def run(self):
        pass

    @property
    def exceptionThrown(self):
        return self._exceptionThrown
    
    @exceptionThrown.setter
    def exceptionThrown(self, isThrown):
        self._exceptionThrown = isThrown

    def getNextTask(self):
        return None
        
    def hasNextChild(self):
        return False
    
    def getNextChild(self):
        return None

    @property
    def params(self):
        return self._params
    
    @params.setter
    def params(self, params):
        self._params.update(params)

