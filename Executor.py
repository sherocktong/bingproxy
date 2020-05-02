'''
Created on 2020年5月1日

@author: shero
'''

            
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
        self.task.run()
        
    def __execute(self, task):
        if not task.exceptionThrown :
            task.run()
            if not task.exceptionThrown:
                while task.hasNextChild():
                    self.__execute(task.getNextChild())
                if (task.next):
                    self.__execute(task.next)
