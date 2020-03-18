class A:      # クラスAを定義
    def method(self):
        print("クラスAです")
 
class B:      # クラスBを定義
    def method(self):
        print("クラスBです")
 
class C(A,B):
    pass      # 何も処理をしない
 
c = C()
c.method()