
import subprocess
from abc import abstractmethod

class ExtExecutionException(Exception):
    pass

class ExtProcessUtil(object):

    @abstractmethod
    def execute(self, statement):
        pass
        
    
class ExtProcessShellUtil(ExtProcessUtil):

    def execute(self, statement):
        statusCode, responseText = subprocess.getstatusoutput(statement)
        if statusCode == -1:
            raise ExtExecutionException() 
        return responseText
