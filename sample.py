from bingproxy.proxy import ProxyDecorator, InvocationHandler

# Invocation Handler handles methond invocation ONLY. Customized handlers must extends from InvocationHandler.        
class CustomizedInvocationHandler(InvocationHandler):
    # Invocation Handler doesn't support the initialization function with parameters.
    def __init__(self):
        print("Hello Handler")
    
    # proxy is the proxy instance which proxies the nested object.
    # func is the raw function invoked.
    # nestedObj is the object which is proxied. It is the object of class CoreClass.
    def invoke(self, proxy, func, nestedObj, *args, **kwargs):
        print("print " + nestedObj.param2 + " previously.")
        return func(*args, **kwargs)

# Use decorator declaration to activate dynamic proxy.
@ProxyDecorator(CustomizedInvocationHandler)
class CoreClass(object):
    def __init__(self, param1, param2):
        super().__init__()
        self.__param1 = param1
        self.__param2 = param2
    
    @property
    def param2(self):
        return self.__param2
    
    def makeThingsDone(self, param3):
        print("nested print: " + param3)
        return True

if __name__ == "__main__":
    instance = CoreClass().newInstance("Hello1", "Hello2")
    finished = instance.makeThingsDone("Hello3")
    if finished is True:
        print("Good Job.")
    else:
        print("Maybe next time.")