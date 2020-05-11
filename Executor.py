from bingdog.Task import TaskExecutionException

class TaskExecutor():

    def __init__(self):
        self._task = None

    @property
    def task(self):
        return self._task
    
    @task.setter
    def task(self, task):
        self._task = task
        
    def execute(self):
        if (self.task):
            self.__execute(self.task)
        
    def __execute(self, task):
        if (task):
            try:
                task.run()
                while task.hasNextChild():
                    self.__execute(task.getNextChild())
                nextTask = task.getNextTask()
                if (nextTask):
                    self.__execute(nextTask)
            except TaskExecutionException as e:
                print(e)
