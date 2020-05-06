
from abc import abstractmethod
from bingdog.Task import Task


class TaskHandler(object):

    def __init__(self):
        self._task = None
        self._childIndex = 0

    @property
    def task(self):
        return self._task
    
    def handle(self):
        self._task = self._createTask()
        self._task.taskHandler = self._getSelfHandler()
        self._prepare(self._task)
        return self.task
    
    @abstractmethod
    def _createTask(self):
        return Task(self)
    
    def _prepare(self, task):
        nextTask = self._getNextTask()
        if (nextTask):
            task.next = self._getNextTask()

    @abstractmethod
    def _getNextTask(self):
        return None
    
    @abstractmethod
    def _getSelfHandler(self):
        return self
    
    def getNextSubTask(self):
        subTask = self._fetchNextSubTask()
        self._childIndex = self._childIndex + 1
        return subTask
    
    @abstractmethod
    def _fetchNextSubTask(self):
        return None
    
    @abstractmethod
    def _getSubTaskListSize(self):
        return 0
    
    def hasMoreSubTask(self):
        if self._childIndex < self._getSubTaskListSize():
            return True
        else:
            return False
