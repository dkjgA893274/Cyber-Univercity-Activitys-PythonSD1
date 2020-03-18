'''対話形式で数字を2個読み取り最小公倍数を求める ver3'''
 
import math
import sys
import sample5_1
 
def myinput(prompt):
    '''引数に指定されたプロンプトメッセージを表示し、キーボードからの入力データを整数として返す。'''
    while True:                #無限ループ
        key = input(f"{prompt}：>> ")
        try:
            key_int = int(key) #文字列として入力された引数を整数に変換
            return key_int     #整数に変換した値を返すことで無限ループを抜ける
        except ValueError:
            print("整数を入力してください")
 
#ここから実行パート
if __name__ == '__main__':
    #myinput関数でキーボードから値を読み込みxに代入
    x = myinput("1つ目の整数を入力してください")
 
    #myinput関数でキーボードから値を読み込みyに代入
    y = myinput("2つ目の整数を入力してください") 
 
    result = sample5_1.lcm(x,y)
    string = f"最小公倍数は{result}です"
 
    file = open('text.txt', 'w') #書き込みモードで開く
    file.write(string) #文字列をファイルに書き込む
    file.close() #ファイルを閉じる
 
    print("ファイルに「"+string+"」と出力しました。") #終了メッセージ