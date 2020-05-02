'''
Created on 2020年5月1日

@author: shero
'''
from abc import abstractmethod


class Task(object):
    
    def __init__(self):
        
        self._next = None
        self._taskHandler = None
        self._params = {}
        self._exceptionThrown = False
    
    @abstractmethod
    def run(self):
        pass
    
    def appendChild(self, task):
        self.subTaskList.append(task)
        
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
        return self._next
    
    @next.setter
    def next(self, task):
        task.params = self.params
        self._next = task
        
    def hasNextChild(self):
        return self._taskHandler.hasMoreSubTask()
    
    def getNextChild(self):
        child = self._taskHandler.getNextSubTask()
        child.params = self.params
        return child

    @property
    def params(self):
        return self._params
    
    @params.setter
    def params(self, params):
        self._params = params
