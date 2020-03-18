class Parent:                # Parentクラスを定義
 
    value = 100
 
    def __init__(self):
        self.value = 200
        
    def getValue(self):
        print("スーパークラスのgetValue( )が実行されました")
        print(self.value)
 
class Child(Parent):         # Parentクラスを継承したChildクラスを定義
 
    def doubleValue(self):   # 新たなメソッドを定義
        self.value = self.value * 2
 
    def getValue(self):      # スーパークラスのgetValueメソッドをオーバーライト
        super().getValue()   # スーパークラスのgetValue( )を実行
        print("サブクラスのgetValue( )が実行されました")
        print(self.value)
 
child = Child()
child.doubleValue()
child.getValue()