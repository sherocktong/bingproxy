from abc import abstractmethod
from bingdog.Task import Task
from bingdog.Proxy import InvocationHandler


class TaskHandler(InvocationHandler):

    def __init__(self, nestedObj, func):
        super(TaskHandler, self).__init__(nestedObj, func)
        self._childIndex = 0

    def __call__(self, *args, **kwargs):
        return self._processMethod(*args, **kwargs)

    def run(self):
        self._nestedObj.run()
        
    def _processMethod(self, *args, **kwargs):
        name = getattr(self._func, '__name__')
        return getattr(self, name)(*args, **kwargs)
        
    def getNextTask(self):
        task = self._getNextTask()
        task.params.update(self._nestedObj.params)
        return task
        
    @abstractmethod
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
        
    @abstractmethod
    def _fetchNextSubTask(self):
        return None
    
    @abstractmethod
    def _getSubTaskListSize(self):
        return 0
