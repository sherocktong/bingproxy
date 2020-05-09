from abc import abstractmethod
from types import MethodType 

class ProxyDecorator(object):

    def __init__(self, handlerClass):
        if issubclass(handlerClass, InvocationHandler) or handlerClass is InvocationHandler:
            self._handlerClass = handlerClass
        else:
            raise HandlerException(handlerClass)
    
    def __call__(self, objClass):
        return Proxy(objClass, self._handlerClass)

class HandlerException(Exception):
    
    def __init__(self, handlerClass):
        super(HandlerException, self).__init__(handlerClass, " is not a class of InvocationHandler.")

class Proxy(object):
    def __init__(self, objClass, handlerClass):
        self._class = objClass
        self._handlerClass = handlerClass

    def __call__(self, *args, **kwargs):
        self._obj = self._class(*args, **kwargs)
        return self
        
    def __getattr__(self, attr):
        exists = hasattr(self._obj, attr)
        res = None
        if exists:
            res = getattr(self._obj, attr)
            if isinstance(res, MethodType):
                return self._handlerClass(self._obj, res)
            else:
                return res
        else:
            return res

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

class InvocationHandler(object):
    def __init__(self, nestedObj, func):
        self._nestedObj = nestedObj
        self._func = func

    def __call__(self, *args, **kwargs):
        return self._processMethod(*args, **kwargs)
    
    def _processMethod(self, *args, **kwargs):
        return self._func(*args, **kwargs)
        