'''コマンド引数の数字を読み取り最小公倍数を求める'''
 
import math
import sys
 
#関数定義パート
def lcm(a, b):
    '''最小公倍数を求める関数'''
    return int(a * b / math.gcd(a, b))
 
#ここから実行パート
if __name__ == '__main__':
    argv = sys.argv
 
    if (len(argv) != 3):
        #引数が2つあるかチェックし、なければメッセージを出力して終了
        print("使い方: python %s 整数1 整数2" % argv[0])
        sys.exit()
 
    x = int(argv[1]) #文字列として入力された引数を整数に変換
    y = int(argv[2]) #int( )関数で整数にキャスト（型を変換）
 
    print("最小公倍数は%dです" % lcm(x,y))