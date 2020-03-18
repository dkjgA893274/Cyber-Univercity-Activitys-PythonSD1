class MyClass:
 
    __value = 100
 
    def __init__(self):
        self.__value = 200
 
    def method(self):
        print("アクセス可能")
 
    def __method(self):
        print("アクセス不可")
 
    def getValue(self):
        print(self.__value)
 
myclass = MyClass()
myclass.method()
myclass.getValue()