class MyClass:
 
    value = 100             # アトリビュートの定義
 
    def __init__(self):     # コンストラクターの定義
        self.value = 200
 
    def getValue(self):     # メソッドの定義
        print(self.value)
 
    def addValue(self):     # メソッドの定義
        self.value += 1
 
myclass = MyClass()
myclass.addValue()
myclass.getValue()