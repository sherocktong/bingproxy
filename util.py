import subprocess
from abc import abstractmethod
import pdb
from types import MethodType
import unicodedata
            
def ifNone(obj) :
    if obj is None:
        raise NullPointerException()
    else:
        return obj
    
class NullPointerException(Exception):
    pass
    
def equalsIgnoreCase(str1, str2):
    if str1 is None or str2 is None:
        return False
    str1 = str1.upper()
    str2 = str2.upper()
    return str1 == str2
    
def implement(baseClass):
    def check(objClass):
        checkIfSubClass(objClass, baseClass)
        return objClass
    return check
    
def checkIfSubClass(objClass, baseClass):
    if not (issubclass(objClass, baseClass) or objClass is baseClass):
        __checkMethodMatching(objClass, baseClass)

def checkIsInstance(obj, baseClass):
    if not isinstance(obj, baseClass):
        __checkMethodMatching(obj, baseClass)
        
def checkIfSameInterface(obj1, obj2):
    __checkMethodMatching(obj1, obj2)

def __checkMethodMatching(objClass, baseClass):
    objMethods = dir(objClass)
    baseMethods = dir(baseClass)
    for name in baseMethods:
        if not name.startswith("_"):
            res = getattr(baseClass, name)
            if isinstance(res, MethodType):
                if not hasattr(objClass, name):
                    raise NotImplementingException(objClass, name, 1)
                else:
                    objRes = getattr(objClass, name)
                    if not isinstance(objRes, MethodType):
                        raise NotImplementingException(objClass, baseClass, name, 1)
                    else:
                        if objRes.__code__.co_argcount != res.__code__.co_argcount:
                            raise NotImplementingException(objRes, baseClass, name, 2)

class NotImplementingException(Exception):
    def __init__(objClass, baseClass, name, exceptionType):
        if exceptionType == 1:
            super().__init__(objClass, "is not implementing method of " + name + " from " + baseClass.__name__ + ".")
        elif exceptionType == 2:
            super().__init__(objClass, "mismatches the number of parameter on method " + name + " from " + baseClass.__name__ + "." )
        
def fetchDict(fromDict):
    toDict = dict()
    if fromDict is None:
        return toDict
    for key in fromDict:
        if not key.startswith('__'):
            toDict[key] = fromDict[key]
    return toDict
    
def trace(func):
    def wrapper(*args, **kwargs):
        pdb.set_trace()
        return func(*args, **kwargs)
    return wrapper
    
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass