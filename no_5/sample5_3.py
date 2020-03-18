'''対話形式で数字を2個読み取り最小公倍数を求める ver2'''
 
import math
import sys
import sample5_1
 
#ここから実行パート
if __name__ == '__main__':
    while True:
        input1 = input('1つ目の整数を入力してください：>> ')
        try:
            x = int(input1) #文字列として入力された引数を整数に変換
            break
        except ValueError:
            print("整数を入力してください")
 
    while True:
        input2 = input('2つ目の整数を入力してください：>> ')
        try:
            y = int(input2) #文字列として入力された引数を整数に変換
            break
        except ValueError:
            print("整数を入力してください")
 
    result = sample5_1.lcm(x,y)
    string = f"最小公倍数は{result}です"
 
    file = open('text.txt', 'w') #書き込みモードで開く
    file.write(string) #文字列をファイルに書き込む
    file.close() #ファイルを閉じる
 
    print("ファイルに「"+string+"」と出力しました。") #終了メッセージ