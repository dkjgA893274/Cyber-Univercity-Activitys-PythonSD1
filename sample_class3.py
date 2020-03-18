class MyClass:
    def __init__(self):
        print('コンストラクターが実行されました')
 
    def __del__(self):
        print('デストラクターが実行されました')
 
myclass = MyClass()
del myclass