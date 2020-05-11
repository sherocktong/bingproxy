from abc import abstractmethod
from bingdog.Task import Task
from bingdog.Proxy import InvocationHandler
from bingdog.ApplicationConfig import Configurator

class MappedInvocationHandler(InvocationHandler):
    def __init__(self):
        self._taskMap = {}
        self._taskObjMap = {}
        
    def _fetchTaskMap(self):
        if len(self._taskMap) == 0:
            self._taskMap = Configurator.configuration['taskMap']

    def _getTaskHandler(self, proxy, nestedObj, *args, **kwargs):
        if self._taskObjMap.get(proxy) is None:
            handlerClass = self._taskMap.get(nestedObj.__module__ + "." + nestedObj.__class__.__name__)
            if handlerClass is None:
                return None
            else:
                self._taskObjMap[proxy] = handlerClass(nestedObj, *args, **kwargs)
        return self._taskObjMap[proxy]
    
    def invoke(self, proxy, func, nestedObj, *args, **kwargs):
        self._fetchTaskMap()
        taskHandler = self._getTaskHandler(proxy, nestedObj, *args, **kwargs)
        if (taskHandler):
            return getattr(taskHandler, func.__name__)(*args, **kwargs)
        else:
            return func(*args, **kwargs)

class TaskHandler(object):

    def __init__(self, nestedObj):
        super().__init__()
        self._childIndex = 0
        self._nestedObj = nestedObj
        
    def run(self):
        self._nestedObj.run()
        
    def getNextTask(self):
        task = self._getNextTask()
        if (task):
            task.params.update(self._nestedObj.params)
        return task
        
    def _getNextTask(self):
        return None
        
    def hasNextChild(self):
        if self._childIndex < self._getSubTaskListSize():
            return True
        else:
            return False
    
    def getNextChild(self):
        subTask = self._fetchNextSubTask()
        subTask.params.update(self._nestedObj.params)
        self._childIndex = self._childIndex + 1
        return subTask
        
    def _fetchNextSubTask(self):
        return None
    
    def _getSubTaskListSize(self):
        return 0
